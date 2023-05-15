#!/usr/bin/env python3
"""implements a caching class from a base class"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """basic cache class"""

    def put(self, key, item):
        if not key or not item:
            return
        self.cache_data[key] = item
