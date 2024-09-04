#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    This function takes an iterable of sequences (e.g., lists or strings) and returns
    a list of tuples. Each tuple contains a sequence and its length.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequences (like lists or strings).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains a sequence
                                     and its length.
    """
    return [(i, len(i)) for i in lst]
