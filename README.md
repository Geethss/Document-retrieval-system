# trademarkia-recruitment-task

Hello Trademarkia Recruiting team,
As per the instructions given, I built a document retrieval system using FastAPI, MongoDB,Redis,Docker and other tools. The system allows for the addition, retrieval, and ranking of documents based on user queries. It uses the BM25 algorithm for initial document retrieval and sentence embeddings for reranking. Additionally, the application features a rate limiter and real-time web scraping for fetching articles.
I even attempted the bonus task where we need to implement re-rank algorithms and fine-tuning scripts for retrievers. Take a look at the features of the project done - 

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

My experience working on this project:
I want to be extremely honest here. I didn't know how to use some of the technologies used in this project before I started working on it. I know all the machine learning related tools as I worked on several projects related to them earlier but I am not familiar with using tools like Docker. I do know that it is a software used for containerization and all the theoretical aspects but never actually worked with it. After researching about the entire project on Google and finding out the best technologies that can be used for each task - That's when I actually sat down to do the task. It took me an entire day - i.e, around 10 hours or so to just research on how to do the task and get familiar with everything. Took some help from online resources like OverStackFlow or medium, whenever I felt struck. I used ChatGPT twice or thrice only when I was not actually able to resolve the error using the above sources. Listing down some of the sources I used for this task - 

1) For getting familiar with FastAPI and issues related to it -
-https://github.com/fastapi/fastapi/issues/2582
-https://fastapi.tiangolo.com/tutorial/handling-errors/#override-request-validation-exceptions
-https://fastapi.tiangolo.com/tutorial/sql-databases/#orms
-https://youtu.be/iWS9ogMPOI0?si=oPQ9xBmA6yoiR5rR

2)For redis related issues -
-https://github.com/redis/redis
-https://redis.io/learn/howtos/quick-start
-https://stackoverflow.com/questions/40678865/how-to-connect-to-remote-redis-server

3)for docker -
-https://medium.com/@anshita.bhasin/a-step-by-step-guide-to-create-dockerfile-9e3744d38d11#id_token=eyJhbGciOiJSUzI1NiIsImtpZCI6ImIyNjIwZDVlN2YxMzJiNTJhZmU4ODc1Y2RmMzc3NmMwNjQyNDlkMDQiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiIyMTYyOTYwMzU4MzQtazFrNnFlMDYwczJ0cDJhMmphbTRsamRjbXMwMHN0dGcuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiIyMTYyOTYwMzU4MzQtazFrNnFlMDYwczJ0cDJhMmphbTRsamRjbXMwMHN0dGcuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMDA0NzM2NjU3OTQ4ODA0NTgxMTkiLCJlbWFpbCI6InBzcmlnZWV0aGFuamFsaUBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwibmJmIjoxNzI2Mzk5MzI5LCJuYW1lIjoiR2VldGhhbmphbGkiLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUNnOG9jS3FNUmQ4aTRjMDZHOXYxOS1JS3VJbDZKc0JjcUdmNVhBN2ZTc0xaTTFJQWo2RW5qaz1zOTYtYyIsImdpdmVuX25hbWUiOiJHZWV0aGFuamFsaSIsImlhdCI6MTcyNjM5OTYyOSwiZXhwIjoxNzI2NDAzMjI5LCJqdGkiOiIwNDU0ZDdiMzQzMTc5Yzc4NTI0ZDI0YzhjZmJmYThlZjYyODMyOTI1In0.oYkv8OMqyn_rbU6yuwxtm0gE0WwYvmsmEb-aakmsz574d_ZhC05M1zYTRPEj_Rmx_8PLwBHFgkWSwnJySnjLSqkgiJj66BoilyCwSRThjU-9ZENHXUr_u1JnN9orgg1fmanSP6EkXv58KLJ54p35Tjz8rXo15pGxUKOeDyCHJg-c18IEd0iLALUx2ju0Pki1PDCEvaGwtrLYpAOfsk6kV-CT3e_HQ203eWiv5Htz-hvwq9UXZSTtM6qI8NYpeD3xRXCZT0tPSd7Z6TqGmVEjR4SfoYF2lUax8UQtao9OnXurzGSD0y2c1IvRRQZ2UkriZc75GsebQGagQ2o--Jp96w

I had to face many small and silly issues, like getting errors when installing the packages in requirements.txt where the tokenizers where not getting installed. It was showing the error that it was not able to build wheels. I scratched my brain for it, installed packages like rust and cargo but still the error was not resolved. In the end, I just tried downloading a different version of tokenizers and Voila, it worked!! The other silly error I did was uploading my virtual environment files to git by mistake and had to remove all of them. Updated gitignore and solved that issue. These two issues are just a glimpse. There are many others I had to face while developing it. This project actually made me feel so dumb and intelligent at the same time sometimes. It was a very great learning curve. Finally, I am grateful to Trademarkia for providing me this oppurtunity to learn.  Sorry if you felt the writing to be too informal.
