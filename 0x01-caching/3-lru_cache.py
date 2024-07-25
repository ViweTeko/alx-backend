#!/usr/bin/env python3
"""LRU Caching file"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """This class implements caching system with LRU eviction"""

    def __init__(self):
        """Initializer"""
        super().__init__()
        self.cache_data = OrderedDict()

    def get(self, key):
        """Returns value linked to key"""
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None

    def put(self, key, item):
        """Implements LRU eviction caching system"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        self.cache_data[key] = item
        if (len(self.cache_data)) > self.MAX_ITEMS:
            old_key, old_val = self.popitem(last=False)
            print(f'DISCARD: {old_key}')
