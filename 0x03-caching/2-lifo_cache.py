#!/usr/bin/python3
""" 1-lifo_cache """
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache (BaseCaching):
    """
    A caching system LIFO
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Adds to cache with limit
        """
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_item = sorted(self.cache_data)[-1]
            self.cache_data.pop(last_item)
            print('DISCARD:', last_item)
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get item with key from cache
        """
        return self.cache_data.get(key, None)
