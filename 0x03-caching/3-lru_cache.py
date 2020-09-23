#!/usr/bin/python3

"""
3. LRU caching
"""

BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """
    Caching based on LRU (least recently used)
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
            least_used = min(self.counter, key=self.counter.get)
            print(self.counter)
            self.cache_data.pop(least_used)
            self.counter.pop(least_used)
            print('DISCARD:', least_used)
        if key and item:
            self.cache_data[key] = item
            self.counter[key] = self.total_count
            self.total_count += 1

    def get(self, key):
        """
        Get item with key from cache
        """
        self.counter[key] = self.total_count
        self.total_count += 1
        return self.cache_data.get(key, None)
