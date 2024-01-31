#!/usr/bin/env python3
"""Module implementing a FIFO cache system"""
from collections import deque

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """A class representing a FIFO cache system."""
    def __init__(self):
        """Initialize the FIFO cache."""
        super().__init__()
        self.insertion_order = deque()

    def put(self, key, item):
        """Add an item to the cache."""
        if not key and not item:
            return None
        if self.cache_data.get(key) != item:
            self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            # Get the key of the first inserted item (FIFO eviction)
            descarded_key = self.insertion_order.popleft()
            del self.cache_data[descarded_key]
            print(f"DISCARD: {descarded_key}")
        self.insertion_order.append(key)

    def get(self, key):
        """Retrieve an item from the cache."""
        return self.cache_data.get(key, None)
