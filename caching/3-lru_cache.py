#!/usr/bin/env python3
"""Creating a LRUCache class
"""
from base_caching import BaseCaching

class LRUCache(BaseCaching):
    """ Class that inherits from BaseCaching"""

    def __init__(self):
      super().__init__()

    def put(self, key, item):
      """El método put agregarán a la caché."""
      if key is None or item is None:
        return
      if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
        print("DISCARD: {}".format(self.last_key))
        self.cache_data.pop(self.last_key)
        self.last_key = key

    def get(self, key):
        """ Return the value linked """
        if key is None or self.cache_data.get(key) is None:
            return
        if key in self.cache_data:
            value = self.cache_data[key]
            return value
