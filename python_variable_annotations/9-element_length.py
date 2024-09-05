#!/usr/bin/env python3
"""
iterable of sequences and returns a list of tuples. 

The function is useful for processing collections of sequences,
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples,
    Args:
        lst (Iterable[Sequence]):  
    Returns:
        List[Tuple[Sequence, int]]:
    """
    return [(i, len(i)) for i in lst]
