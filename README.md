# Document-retrieval-system

Built a document retrieval system using FastAPI, MongoDB,Redis,Docker and other tools. The system allows for the addition, retrieval, and ranking of documents based on user queries. It uses the BM25 algorithm for initial document retrieval and sentence embeddings for reranking. Additionally, the application features a rate limiter and real-time web scraping for fetching articles. Also Implemented re-rank algorithms and fine-tuning scripts for retrievers. Take a look at the features of the project done - 

## Features
- **Document Insertion**: Add new documents to the MongoDB database.
- **BM25 Search**: Perform initial document retrieval using the BM25 algorithm.
- **Reranking with Sentence Embeddings**: Enhance search results by reranking based on similarity using sentence embeddings.
- **Rate Limiting**: Restrict user requests to prevent abuse, using Redis for tracking.
- **Web Scraping**: Automatically scrape articles from a news website at startup.
- **Logging**: Log all incoming requests and responses to monitor application behavior.

  
## Technologies Used
- **FastAPI**: Web framework for building APIs.
- **MongoDB (AsyncIO)**: NoSQL database for storing documents.
- **Redis**: In-memory data structure store, used for rate limiting.
- **BM25**: Algorithm for ranking documents based on term frequency.
- **Transformers (Hugging Face)**: For sentence embeddings.
- **BeautifulSoup**: For web scraping.
- **Loguru**: For structured logging.
- **Threading**: To handle background web scraping tasks.
- **Docker**: For containerizing the application.
