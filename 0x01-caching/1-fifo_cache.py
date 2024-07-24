#!/usr/bin/env python3
"""FIFO Caching file"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """This class implements caching system with FIFO eviction"""

    def __init__(self):
        """Initializer"""
        super().__init__()
        self.queue = []

    def get(self, key):
        """Returns value linked to key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]

    def put(self, key, item):
        """Implements FIFO eviction if cache reaches max"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) >= self.MAX_ITEMS:
                old_key = self.queue.pop(0)
                del self.cache_data[old_key]
                print(f'DISCARD: {old_key}')
            self.cache_data[key] = item
            self.queue.append(key)
        else:
            self.cache_data[key] = item
