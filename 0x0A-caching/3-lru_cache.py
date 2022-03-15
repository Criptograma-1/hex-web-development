#!/usr/bin/python3
"""
Basic dictionary LRUCache Cache
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache Caching System"""

    def __init__(self) -> None:
        """Init function"""
        super().__init__()
        self.list_name = []

    def put(self, key, item):
        """Put function"""
        if key and item:
            self.cache_data[key] = item
            if key not in self.list_name:
                self.list_name.append(key)
            else:
                if self.list_name[-1] != key:
                    self.list_name.remove(key)
                    self.list_name.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(self.list_name[0]))
                del(self.cache_data[self.list_name[0]])
                self.list_name.pop(0)

    def get(self, key):
        """Get function"""
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.list_name:
            if self.list_name[-1] != key:
                self.list_name.remove(key)
                self.list_name.append(key)

        return self.cache_data[key]
