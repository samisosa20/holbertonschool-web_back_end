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
        ''' Initialize class instance. '''
        super().__init__()
        self.keys = []

    def put(self, key, item):
        ''' Add key/value pair to cache data.
            If cache is at max capacity (specified by BaseCaching.MAX_ITEMS),
            discard least recently used entry in cache to accommodate new
            entry. '''
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(0)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        ''' Return value stored in `key` key of cache.
            If key is None or does not exist in cache, return None. '''
        if key is not None and key in self.cache_data:
            self.keys.append(self.keys.pop(self.keys.index(key)))
            return self.cache_data[key]
        return None
