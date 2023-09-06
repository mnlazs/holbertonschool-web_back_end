#!/usr/bin/env python3
"""La función 'to_kv' calcula la cadena de un número flotante."""
from typing import KeysView, Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Toma una cadena y un número entero o flotante, y devuelve una tupla.
    
    El primer elemento de la tupla es la cadena k, y el segundo elemento
    es el cuadrado del número v, anotado como un número flotante.
    
    :param k: Una cadena.
    :type k: str
    
    :param v: Un número entero o flotante.
    :type v: Union[int, float]
    
    :return: Una tupla con el valor de k y el cuadrado de v.
    :rtype: Tuple[str, float]
    """
    
    return (k, v * v)
















