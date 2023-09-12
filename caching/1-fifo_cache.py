#!/usr/bin/env python3
"""Creating a FIFOCache class
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Class that inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """El método put representan la clave y el valor
              que se agregarán a la caché."""
        if key is not None and item is not None:

            # Verificar si el número de elementos supera el límite
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:

                # Aplicar el algoritmo FIFO eliminando el elemento mas antiguo
                key_discard = next(iter(self.cache_data))
                self.cache_data.pop(key_discard)
                # imprimir mensaje de descarte
                print("DISCARD:", key_discard)

        # Asignar el valor item a la clave key en la caché
        self.cache_data[key] = item

    def get(self, key):
        """ Return the value """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
