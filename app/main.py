from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import time
import json
from app.db import get_cache, set_cache

app = FastAPI()

# Dummy database of documents
documents = [
    {"id": 1, "content": "Document about AI and machine learning."},
    {"id": 2, "content": "Document about climate change and sustainability."},
    {"id": 3, "content": "Document about blockchain and decentralized applications."}
]

@app.get("/health")
def health_check():
    return {"status": "API is active"}

class SearchRequest(BaseModel):
    text: str
    top_k: int = 5
    threshold: float = 0.5

@app.post("/search")
def search(request: SearchRequest):
    start_time = time.time()

    cache_key = f"search:{request.text}:{request.top_k}:{request.threshold}"
    cached_results = get_cache(cache_key)

    if cached_results:
        results = json.loads(cached_results)
    else:
        results = documents[:request.top_k]
        set_cache(cache_key, json.dumps(results), ex=60)  # Cache for 1 minute

    inference_time = time.time() - start_time
    return {"results": results, "inference_time": inference_time}

import threading
import requests
from bs4 import BeautifulSoup

def scrape_articles():
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    articles = [a.text for a in soup.find_all("a", class_="storylink")]
    print("Scraped articles:", articles)  # Replace with saving to a database or cache

@app.on_event("startup")
async def startup_event():
    threading.Thread(target=scrape_articles, daemon=True).start()
