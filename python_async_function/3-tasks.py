#!/usr/bin/env python3
"""Import wait_random from the previous python file"""
import asyncio
from typing import Any
from random import uniform
from asyncio import Task

async def wait_random(max_delay: int = 10) -> float:
    """Función asincrónica que espera un tiempo aleatorio entre 0 y max_delay."""
    random_float = uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float

def task_wait_random(max_delay: int) -> Task[Any]:
    """Función que crea una tarea asincrónica que ejecuta wait_random(max_delay)."""
    return asyncio.create_task(wait_random(max_delay))
