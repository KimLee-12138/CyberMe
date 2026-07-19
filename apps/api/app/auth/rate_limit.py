"""Rate limiting using Redis counters."""

import hashlib
import time

import redis.asyncio as aioredis

from app.core.config import settings


class RateLimiter:
    """Simple sliding-window rate limiter backed by Redis."""

    def __init__(self, redis_url: str | None = None):
        self._redis_url = redis_url or settings.redis_url
        self._redis: aioredis.Redis | None = None

    async def _get_redis(self) -> aioredis.Redis:
        if self._redis is None:
            self._redis = aioredis.from_url(self._redis_url, decode_responses=True)
        return self._redis

    def _key(self, prefix: str, identifier: str) -> str:
        hashed = hashlib.sha256(identifier.encode()).hexdigest()[:16]
        return f"ratelimit:{prefix}:{hashed}"

    async def check(
        self,
        prefix: str,
        identifier: str,
        max_requests: int,
        window_seconds: int,
    ) -> bool:
        """
        Check if the action is within the rate limit.
        Returns True if allowed, False if rate-limited.
        """
        try:
            r = await self._get_redis()
            key = self._key(prefix, identifier)
            now = int(time.time())

            # Remove old entries
            await r.zremrangebyscore(key, 0, now - window_seconds)

            # Count requests in the current window
            count = await r.zcard(key)

            if count >= max_requests:
                return False

            # Add this request
            await r.zadd(key, {str(now): now})
            await r.expire(key, window_seconds + 10)

            return True
        except Exception:
            # If Redis is unavailable, allow the request
            return True

    async def reset(self, prefix: str, identifier: str) -> None:
        """Reset the rate limit for a given key."""
        try:
            r = await self._get_redis()
            key = self._key(prefix, identifier)
            await r.delete(key)
        except Exception:
            pass


# Global singleton
rate_limiter = RateLimiter()
