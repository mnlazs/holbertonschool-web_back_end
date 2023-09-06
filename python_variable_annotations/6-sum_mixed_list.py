#!/usr/bin/env python3
""" Complex types - list of floats """
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Sum lista de números flot y return la sum número flotante.

    :param input_list: Una lista de números flotantes.
    :type input_list: List[float]

    :return: La suma de los números flotantes en la lista.
    :rtype: float
"""
    return sum(mxd_list)
