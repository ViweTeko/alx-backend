#!/usr/bin/env python3
"""MRU Caching file"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """This class implements caching system with MRU eviction"""

    def __init__(self):
        """Initializer"""
        super().__init__()
        self.cache_data = {}
        self.keys = []

    def get(self, key):
        """Returns value linked to key"""
        if key in self.cache_data:
            self.keys.remove(key)
            self.keys.append(key)
            return self.cache_data[key]
        return None

    def put(self, key, item):
        """Implements MRU eviction caching system"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.keys.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            recent_key = self.keys.pop()
            del self.cache_data[recent_key]
            print(f'DISCARD: {recent_key}')
        self.cache_data[key] = item
        self.keys.append(key)
