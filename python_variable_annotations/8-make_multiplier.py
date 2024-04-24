#!/usr/bin/env python3
""" takes a float multiplier as argument and returns a function that multiplies a float by multiplier"""  # noqa
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """takes a float multiplier as argument and returns a function that multiplies a float by multiplie"""  # noqa
    def multiply(value: float) -> float:
        return value * multiplier
    return multiply
