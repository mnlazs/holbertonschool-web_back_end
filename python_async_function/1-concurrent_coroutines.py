#!/usr/bin/env python3
"""Import wait_random from the previous python file"""
from typing import List
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """Función asincrónica q espera un tiempo aleatorio entre 0 y max_delay."""
    random_float = uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Función que invoca wait_random n veces y devuelve una lista"""
    delays = []
    tasks = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)
    for task in tasks:
        await task
        delays.append(task.result())
    return sorted(delays)
