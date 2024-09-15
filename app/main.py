from fastapi import FastAPI, HTTPException, Depends, Request
from pydantic import BaseModel
import time
from rank_bm25 import BM25Okapi
from transformers import pipeline
from sklearn.metrics.pairwise import cosine_similarity
from motor.motor_asyncio import AsyncIOMotorClient
import threading
import requests
from bs4 import BeautifulSoup
from app.db import redis_client
from loguru import logger

app = FastAPI()

class SearchRequest(BaseModel):
    text: str
    top_k: int = 5  
    threshold: float = 0.5 

bm25_search_model = pipeline("feature-extraction", model="sentence-transformers/all-MiniLM-L6-v2")

def bm25_search(query, documents, top_k):
    tokenized_docs = [doc["content"].split(" ") for doc in documents]
    bm25 = BM25Okapi(tokenized_docs)
    doc_scores = bm25.get_scores(query.split(" "))
    top_indices = sorted(range(len(doc_scores)), key=lambda i: doc_scores[i], reverse=True)[:top_k]
    return [documents[i] for i in top_indices]

def rerank(query, documents):
    query_embedding = bm25_search_model(query)[0]
    doc_embeddings = [bm25_search_model(doc["content"])[0] for doc in documents]
    similarities = [cosine_similarity([query_embedding], [doc_emb])[0][0] for doc_emb in doc_embeddings]
    ranked_docs = sorted(zip(documents, similarities), key=lambda x: x[1], reverse=True)
    return [doc for doc, _ in ranked_docs]

MONGO_URI = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_URI)
db = client["document_db"]  
collection = db["documents"]  

async def get_collection():
    return collection

class Document(BaseModel):
    content: str

@app.post("/documents")
async def add_document(document: Document, collection=Depends(get_collection)):
    result = await collection.insert_one(document.dict())
    return {"document_id": str(result.inserted_id)}

async def fetch_documents(query: dict, collection=Depends(get_collection)):
    cursor = collection.find(query)
    documents = await cursor.to_list(None)
    return documents

@app.post("/search")
async def search(request: SearchRequest, collection=Depends(get_collection)):
    start_time = time.time()
    documents = await fetch_documents({}, collection)
    bm25_results = bm25_search(request.text, documents, request.top_k)
    reranked_results = rerank(request.text, bm25_results)
    inference_time = time.time() - start_time
    return {"results": reranked_results, "inference_time": inference_time}

def scrape_articles():
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    articles = [a.text for a in soup.find_all("a", class_="storylink")]
    print("Scraped articles:", articles)

@app.on_event("startup")
async def startup_event():
    threading.Thread(target=scrape_articles, daemon=True).start()
    await collection.create_index("content")

RATE_LIMIT = 5

@app.middleware("http")
async def rate_limiter(request: Request, call_next):
    user_id = request.headers.get("user_id")
    if not user_id:
        raise HTTPException(status_code=400, detail="user_id is required")
    
    user_key = f"user:{user_id}:requests"
    request_count = redis_client.get(user_key)

    if request_count and int(request_count) >= RATE_LIMIT:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")
    
    redis_client.incr(user_key)
    redis_client.expire(user_key, 60)

    response = await call_next(request)
    return response

logger.add("file.log", rotation="1 MB")

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Incoming request: {request.url.path}, User: {request.headers.get('user_id')}")
    response = await call_next(request)
    logger.info(f"Response status: {response.status_code}")
    return response


