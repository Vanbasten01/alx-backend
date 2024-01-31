#!/usr/bin/env python3
"""Module implementing a FIFO cache system"""

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """A class representing a FIFO cache system."""
    def __init__(self):
        """Initialize the FIFO cache."""
        super().__init__()
        self.insertion_order = []

    def put(self, key, item):
        """Add an item to the cache."""
        if not key or not item:
            return None
        if self.cache_data.get(key) != item:
            self.cache_data[key] = item
            if key not in self.insertion_order:
                self.insertion_order.append(key)
        if len(self.cache_data) > self.MAX_ITEMS:
            # Get the key of the first inserted item (FIFO eviction)
            descarded_key = self.insertion_order.pop(0)
            del self.cache_data[descarded_key]
            print(f"DISCARD: {descarded_key}")

    def get(self, key):
        """Retrieve an item from the cache."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
