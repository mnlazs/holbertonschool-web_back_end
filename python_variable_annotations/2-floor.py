#!/usr/bin/env python3
"""Módulo que contiene la función 'floor' para calcular el entero inferior de un número flotante."""
import math


def floor(n: float) -> int:
    """
    type-annotated function floor.
    :param n: A floating-point number.
    :type n: float

    :return: The floor (integer) of the input float.
    :rtype: int
    """
    return math.floor(n)
