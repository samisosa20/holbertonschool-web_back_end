#!/usr/bin/python3
""" 0-basic_cache """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    A caching system
    """

    def put(self, key, item):
        """
        Adds to cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get item with key from cache
        """
        return self.cache_data.get(key, None)
