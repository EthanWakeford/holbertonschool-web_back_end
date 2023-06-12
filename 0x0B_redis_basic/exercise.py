#!/usr/bin/env python3
"""holds a cache class"""
import redis
from uuid import uuid4
from typing import Union


class Cache():
    """defines a cache"""

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """creates a key and stores into redis"""
        key = str(uuid4())
        self._redis.set(key, data)

        return key