#!/usr/bin/env python3
"""Creating a BaseCaching class
"""
from base_caching import BaseCaching

# Definicion de la super clase
class BasicCache(BaseCaching):
    """ Class that inherits from BaseCaching and is a caching system
        This caching system doesn’t have limit """
    def __init__(self):
        """ Initiliaze
        """
        super().___init__()
        
    def put(self, key, item):
      """El método put representan la clave y el valor 
          que se agregarán a la caché."""
      if key is None or item is None:
        self.cache_data[key] = item
          
    def get(self, key):
          """ Return the value """
          if key is None or key not in self.cache_data:
            return None
          return self.cache_data[key]