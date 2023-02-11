from redis.asyncio import Redis, from_url

from .environment import REDIS_HOST, REDIS_PORT


redis: Redis = await from_url(
    f"redis://{REDIS_HOST}:{REDIS_PORT}", encoding="utf-8", decode_responses=True
)
