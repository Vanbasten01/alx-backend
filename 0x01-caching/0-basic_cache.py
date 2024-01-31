#!/usr/bin/env python3
"""Module implementing a basic cache system"""

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """A basic cache class extending BaseCaching."""
    def __init__(self):
        """Initialize the BasicCache."""
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache."""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache."""
        return self.cache_data.get(key, None)
