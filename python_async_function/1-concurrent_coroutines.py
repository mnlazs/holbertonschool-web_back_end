#!/usr/bin/env python3
"""Import wait_random from the previous python file"""
from typing import List
import asyncio
from random import uniform

wait_random = __import__('0-basic_async_syntax').wait_random


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
