#!/usr/bin/python3

"""
4. MRU caching
"""

BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """
    Caching based on MRU (Most recently used)
    """

    def __init__(self):
        super().__init__()
        self.total_count = 0
        self.counter = {}

    def put(self, key, item):
        """
        Add key/item pair into cache.
        If cache is full, remove the first item and add the new item
        """
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            most_used = max(self.counter, key=self.counter.get)
            self.cache_data.pop(most_used)
            print('DISCARD:', most_used)
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get item with key from cache
        """
        self.total_count += 1
        self.counter[key] = self.total_count
        return self.cache_data.get(key, None)
