#!/usr/bin/python3
"""
Basic dictionary FIFO Cache
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """BaseCaching Caching System"""

    def __init__(self) -> None:
        """Init function"""
        super().__init__()

    def put(self, key, item):
        """Put function"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                firstItem = list(self.cache_data.keys())[0]
                print("DISCARD: {}".format(firstItem))
                del(self.cache_data[firstItem])

    def get(self, key):
        """Get function"""
        if key is not None:
            for k, value in self.cache_data.items():
                if k == key:
                    return value
        return None
