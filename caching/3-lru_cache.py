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
        # Encuentra la clave del elemento menos recientemente utilizado (LRU)
        lru_key = None
        for k in self.cache_data:
            if lru_key is None or self.cache_data[k]["accessed_at"] < self.cache_data[lru_key]["accessed_at"]:
                lru_key = k

        # Elimina el elemento LRU de la caché
        del self.cache_data[lru_key]
        print(f"DISCARD: {lru_key}")

    # Agrega el nuevo elemento a la caché
      self.cache_data[key] = {"value": item, "accessed_at": self.current_time}
      self.current_time += 1
      def get(self, key):
        """ Return the value linked """
        if key is None or self.cache_data.get(key) is None:
            return
        if key in self.cache_data:
            value = self.cache_data[key]
            return value
