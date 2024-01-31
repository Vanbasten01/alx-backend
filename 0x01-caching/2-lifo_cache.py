#!/usr/bin/env python3
"""module for the class LIFOCache"""

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """A class representing a LIFO cache system."""
    def __init__(self):
        """Initialize the LIFO cache."""
        super().__init__()
        self.insertion_order = []

    def put(self, key, item):
        """Add an item to the cache."""
        if key is None or item is None:
            return None
        if self.cache_data.get(key) != item:
            self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            last_key = self.insertion_order.pop()
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")
        self.insertion_order.append(key)

    def get(self, key):
        """Retrieve an item from the cache."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
