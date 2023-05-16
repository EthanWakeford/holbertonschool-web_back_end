#!/usr/bin/env python3
"""implements an lru caching class from a base class"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """makes an lru cache"""
    def __init__(self):
        super().__init__()
        self.access_log = []

    def put(self, key, item):
        """puts a value into cache"""
        if not key or not item:
            return
        if len(self.cache_data) == self.MAX_ITEMS:
            last_key = self.access_log.pop(0)
            del self.cache_data[last_key]
            print('DISCARD: ' + last_key)
        self.cache_data[key] = item
        self.access_log.append(key)

    def get(self, key):
        """gets value from cache"""
        if not key or key not in self.cache_data:
            return None
        self.access_log.pop(self.access_log.index(key))
        self.access_log.append(key)
        return self.cache_data[key]
