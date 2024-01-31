#!/usr/bin/env python3
""" Module for LFUCache """
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class inherits from BaseCaching """
    def __init__(self):
        """ Initialize LFUCache """
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """ Add an item to the cache """
        if not key or not item:
            return None
        if self.get(key) != item:
            self.cache_data[key] = item

            if len(self.cache_data) > self.MAX_ITEMS:
                lfu_key = min(self.frequency, key=self.frequency.get)
                del self.cache_data[lfu_key]
                print(f"DISCARD: {lfu_key}")
                self.frequency.pop(lfu_key)
            if key not in self.frequency:
                self.frequency[key] = 0

    def get(self, key):
        """ Get an item from the cache """
        if not key or key not in self.cache_data:
            return None
        else:
            self.frequency[key] += 1
            return self.cache_data[key]
