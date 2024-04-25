#!/usr/bin/env python3
""""""

import asyncio
from typing import List
from time import time



async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an asynchronous comprehension over async_generator.
    """
    return [number async for number in async_generator()]


async def measure_runtime() -> float:
    """
    Measures the total runtime of executing async_comprehension four times in parallel.
    """
    start_time = time()

    # Execute async_comprehension four times in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time()
    total_runtime = end_time - start_time
    return total_runtime