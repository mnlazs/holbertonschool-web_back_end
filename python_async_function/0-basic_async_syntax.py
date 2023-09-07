#!/usr/bin/env python3
""" The basics of async  """
import random
import asyncio


async def wait_random(max_delay=10):
  # Generar un valor de espera aleatorio entre 0 y max_delay (incluyendo decimales)
  delay = random.uniform(0, max_delay)
  
  # Esperar durante el tiempo aleatorio generado
  await asyncio.sleep(delay)
  
  # Devolver la duración real de la espera
  return delay  