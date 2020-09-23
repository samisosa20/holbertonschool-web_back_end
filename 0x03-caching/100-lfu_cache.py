
#!/usr/bin/python3

"""
100. LFU caching
"""

BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """
    Caching based on LRU (least frequently used)
    """

    def __init__(self):
        super().__init__()
        self.total_count = 0
        self.counter = {}
        self.frequency = {}

    def put(self, key, item):
        """
        Add key/item pair into cache.
        If cache is full, remove the first item and add the new item
        """
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            least_used = min(self.counter, key=self.counter.get)
            self.cache_data.pop(least_used)
            print('DISCARD:', least_used)
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get item with key from cache
        """
        self.total_count += 1
        self.counter[key] = self.total_count
        if key not in self.frequency:
            self.frequency[key] = 1
        else:
            self.frequency[key] += 1
        return self.cache_data.get(key, None)
