#!/usr/bin/env python3
"""Creating a BaseCaching class
"""
from base_caching import BaseCaching

# Definicion de la super clase
class BasicCache(BaseCaching):
    """ BaseCache defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    def __init__(self):
        """ Initiliaze
        """
        super().___init__()
        
    def put(self, key, item):
          if key is None or item is None:
            return
          self.cache_data[key] = item
          
    def get(self, key):
          if key is None or key not in self.cache_data:
            return None
          
          return self.cache_data[key]