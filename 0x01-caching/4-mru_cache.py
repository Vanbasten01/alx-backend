#!/usr/bin/env python3
"""Module for MRU Cache"""


BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class that inherits from BaseCaching"""
    def __init__(self):
        """Initialize MRUCache"""
        super().__init__()
        self.mru_keys = []

    def put(self, key, item):
        """Put method to add or update an item in the cache"""
        if not key or not item:
            return None

        if self.cache_data.get(key) != item:
            self.cache_data[key] = item
            self.mru_keys.append(key)

        if len(self.cache_data) > self.MAX_ITEMS:
            mru_key = self.mru_keys.pop(-2)
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

    def get(self, key):
        """Get method to retrieve an item from the cache"""
        if not key or key not in self.cache_data:
            return None
        else:
            self.mru_keys.append(key)
            return self.cache_data.get(key)
