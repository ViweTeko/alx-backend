#!/usr/bin/env python3
""" A caching system with LFU eviction policy."""
from base_caching import BaseCaching
from collections import OrderedDict, defaultdict


class LFUCache(BaseCaching):
    """LFU eviction policy."""

    def __init__(self):
        """Initializer"""
        super().__init__()
        self.cache_data = OrderedDict()
        self.frequency = defaultdict(int)
        self.usage_order = OrderedDict()

    def get(self, key):
        """Return the value linked to key."""
        if key in self.cache_data:
            self.frequency[key] += 1
            self.usage_order.move_to_end(key)
            return self.cache_data[key]
        return None

    def put(self, key, item):
        """Maintain LFU order caching"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.usage_order.move_to_end(key)
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                min_freq = min(self.frequency.values())
                lfu_keys = [k for k, v in self.frequency.items()
                            if v == min_freq]
                if len(lfu_keys) > 1:
                    lfu_key = next(
                        k for k in self.usage_order if k in lfu_keys)
                else:
                    lfu_key = lfu_keys[0]

                del self.cache_data[lfu_key]
                del self.frequency[lfu_key]
                del self.usage_order[lfu_key]
                print(f'DISCARD: {lfu_key}')

            self.cache_data[key] = item
            self.frequency[key] = 1
            self.usage_order[key] = None
