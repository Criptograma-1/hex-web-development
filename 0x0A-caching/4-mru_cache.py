#!/usr/bin/python3
"""
Basic dictionary MRU Cache
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache Caching System"""

    def __init__(self) -> None:
        """Init function"""
        super().__init__()
        self.__keys = []

    def put(self, key, item):
        """Put function"""
        if len(self.cache_data) == self.MAX_ITEMS and key not in self.__keys:
            discard = self.__keys.pop()
            del self.cache_data[discard]
            print('DISCARD: {}'.format(discard))
        if key and item:
            if key not in self.__keys:
                self.__keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Get function"""
        if key is None or self.cache_data.get(key) is None:
            return None
        self.__keys.remove(key)
        self.__keys.append(key)
        return self.cache_data[key]
