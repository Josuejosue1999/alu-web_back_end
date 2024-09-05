#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    returns a list of tuples.
    Args:
        lst (Iterable[Sequence]):
    Returns:
        List[Tuple[Sequence, int]]:
    """
    return [(i, len(i)) for i in lst]
