#!/usr/bin/env python3
"""LIFO Caching file"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """This class implements caching system with LIFO eviction"""

    def __init__(self):
        """Initializer"""
        super().__init__()
        self.stack = []

    def get(self, key):
        """Returns value linked to key"""
        if key is None or key not in self.cache_data:
            return None
        return (self.cache_data.get(key, None))

    def put(self, key, item):
        """Implements LIFO eviction if cache reaches max"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) >= self.MAX_ITEMS:
                new_key = self.stack.pop(0)
                del self.cache_data[new_key]
                print(f'DISCARD: {new_key}')
            self.cache_data[key] = item
            self.stack.append(key)
        else:
            self.cache_data[key] = item
            self.stack.remove(key)
            self.stack.append(key)
