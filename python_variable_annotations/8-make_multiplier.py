#!/usr/bin/env python3
""" Return a funtion  - multiplies a floats """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Toma un multiplicador flotante como argumento y devuelve una función que
    multiplica un número flotante por el multiplicador.

    :param multiplier: Numero flotante q se utilizará para la multiplicación.
    :type multiplier: float

    :return: Una función que toma un número flotante y devuelve el resultado de
    multiplicar ese número por el multiplicador.
    :rtype: Callable[[float], float]
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
