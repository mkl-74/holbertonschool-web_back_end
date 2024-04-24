#!/usr/bin/env python3
"""take a string as arguments and return a tuple"""
from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, v * v)
