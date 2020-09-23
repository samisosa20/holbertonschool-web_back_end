#!/usr/bin/python3
""" 1-fifo_cache """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache (BaseCaching):
    """
    A caching system FIFO
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Adds to cache with limit
        """
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_item = sorted(self.cache_data)[0]
            self.cache_data.pop(first_item)
            print('DISCARD:', first_item)
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get item with key from cache
        """
        return self.cache_data.get(key, None)
