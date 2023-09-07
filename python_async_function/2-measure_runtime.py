#!/usr/bin/env python3
"""Import wait_random from the previous python file"""
from typing import List
import asyncio
import time
from random import uniform


async def wait_random(max_delay: int =10) -> float:
    """Función asincrónica que espera un tiempo aleatorio """
    random_float = uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Función que invoca wait_random n veces y devuelve una lista."""
    delays = []
    tasks = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)
    for task in tasks:
        await task
        delays.append(task.result())
    return sorted(delays)


def measure_time(n: int, max_delay: int) -> float:
    """Mide el tiempo total de ejecución para wait_n """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
