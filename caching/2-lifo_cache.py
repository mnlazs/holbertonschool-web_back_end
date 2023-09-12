#!/usr/bin/env python3
"""Creating a FIFOCache class
"""
from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """ Class that inherits from BaseCaching and is a caching system"""

    def __init__(self):
      """Initialiaze
      """
      super().__init__()
    
    def put(self, key, item):
      """El método donde se agregará a la caché."""
      if key or item is None:
        return

      if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
        last_key = list(self.cache_data.keys())[-1]
        # Eliminamos el último elemento de la caché
        del self.cache_data(last_key)
        print(f"DISCARD: {last_key}\n") 
# Asignar el valor item a la clave key en la caché
      self.cache_data[key] = item