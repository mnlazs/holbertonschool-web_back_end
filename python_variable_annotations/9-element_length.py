#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Toma una lista o secuencia de elementos y devuelve una lista de tuplas.

    Cada tupla contiene dos elementos:
    - El primer elemento es una secuencia (cadena de texto o lista).
    - El 2do element s un núm int que representa la longitud de la secuencia.

    :param lst: Una lista o secuencia de elementos.
    :type lst: Iterable[Sequence]

    :return: List de tuplas y cada tupla contiene una secuencia y su longitud.
    :rtype: List[Tuple[Sequence, int]]
    """
    return [(i, len(i)) for i in lst]
