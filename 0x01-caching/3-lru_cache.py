#!/usr/bin/env python3
"""LRUCache module: Implements a Least Recently Used (LRU) cache."""

from collections import OrderedDict
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class: Implements a Least Recently Used (LRU) cache."""
    def __init__(self):
        """Initialize LRUCache instance."""
        super().__init__()
        self.ordered_dict = OrderedDict()

    def put(self, key, item):
        """Add or update an item in the cache."""
        if not key or not item:
            return None
        if self.cache_data.get(key) != item:
            self.ordered_dict[key] = item
            self.ordered_dict.move_to_end(key)
            self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            lru_key, _ = self.ordered_dict.popitem(last=False)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

    def get(self, key):
        """Retrieve an item from the cache."""
        if not key or key not in self.cache_data:
            return None
        else:
            self.ordered_dict.move_to_end(key)
            return self.cache_data[key]
