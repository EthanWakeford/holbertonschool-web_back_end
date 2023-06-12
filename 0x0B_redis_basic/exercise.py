#!/usr/bin/env python3
"""holds a cache class"""
import redis
from uuid import uuid4
from typing import Union, Callable


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

    def get(self, key: str, fn: Callable = None):
        """gets from redis"""
        if self._redis.exists(key):
            val = self._redis.get(key)
            if (fn):
                val = fn(val)
            return val
        else:
            return

    def get_str(self, key):
        """gets a str from redis"""
        return self.get(key, str)

    def get_int(self, key):
        """gets an int from redis"""
        return self.get(key, int)
