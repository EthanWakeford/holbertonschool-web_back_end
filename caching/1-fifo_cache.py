#!/usr/bin/env python3
"""implements a caching class from a base class"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """a fifo cache example"""

    def put(self, key, item):
        """puts into cache, removes first key if cache is full"""
        if not key or not item:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            self.cache_data.pop(first_key)
            print('DISCARD: ' + first_key)

    def get(self, key):
        """gets value from cache"""
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
