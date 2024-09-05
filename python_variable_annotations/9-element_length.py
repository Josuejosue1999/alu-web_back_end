#!/usr/bin/env python3
"""
This module provides a function that takes an iterable of sequences
and returns a list of tuples. Each tuple contains a sequence and its
corresponding length.

The function is useful for processing collections of sequences, such as
lists of strings or lists of lists, where determining the length of each
sequence is necessary.
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
