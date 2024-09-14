import redis
from app.config import REDIS_URL

redis_client = redis.Redis.from_url(REDIS_URL)

def get_cache(key):
    return redis_client.get(key)

def set_cache(key, value, ex=None):
    redis_client.set(key, value, ex=ex)
