#!/usr/bin/env python3
"""annotate the length of an element in a list"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotate the length of an element in a list"""
    return [(i, len(i)) for i in lst]
