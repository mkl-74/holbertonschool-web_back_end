#!/usr/bin/env python3
"""take a string as arguments and return a tuple"""
from typing import Union, Tuple

def to_kv(k: str, value: float) -> tuple:
    """take a string as arguments and return a tuple"""
    return (k, value**2)
