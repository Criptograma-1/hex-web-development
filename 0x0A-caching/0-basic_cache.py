#!/usr/bin/python3
"""
Basic dictionary
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache that inherits from BaseCaching and is a caching system:
       -use self.cache_data - dictionary from the parent class BaseCaching
       -This caching system doesn’t have limit
    """
    def __init__(self) -> None:
        super().__init__()

    def put(self, key, item):
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        if key is not None:
            for k, value in self.cache_data.items():
                if k == key:
                    return v
        return None
