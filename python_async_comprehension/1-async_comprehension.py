#!/usr/bin/env python3
"""collect 10 random numbers"""


import asyncio  # Add this import statement

from typing import List
from random import uniform

async def async_generator() -> float:
    """
    Coroutine that yields 10 random numbers between 0 and 10 with a 1-second delay.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)

async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an asynchronous comprehension over async_generator.
    """
    return [number async for number in async_generator()]
