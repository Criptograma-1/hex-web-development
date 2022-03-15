#!/usr/bin/python3
"""
Basic dictionary LIFO Cache
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache Caching System"""

    def __init__(self) -> None:
        """Init function"""
        super().__init__()
        self.last = ""

    def put(self, key, item):
        """Put function"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(self.last))
                del(self.cache_data[self.last])
            self.last = key

    def get(self, key):
        """Get function"""
        if key is not None:
            for k, value in self.cache_data.items():
                if k == key:
                    return value
        return None
