#!/usr/bin/env python3
"""written and write an async routine called wait_n"""
import asyncio
from typing import List
from random import uniform


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that takes in 2 int arguments (n and max_delay)
    """
    delays = [wait_random(max_delay) for _ in range(n)]
    return sorted(await asyncio.gather(*delays))


async def wait_random(max_delay: int) -> float:
    """
    Asynchronous coroutine that waits for a random delay between
    0 and max_delay
    """
    return uniform(0, max_delay)
