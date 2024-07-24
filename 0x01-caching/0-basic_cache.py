#!/usr/bin/env python3
"""Basic cache dict"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Child class that is a caching system"""

    def put(self, key, item):
        """Adds an item to cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Returns value linked to key"""
        if key is None or key not in self.cache_data:
            return (None)
        return self.cache_data[key]
