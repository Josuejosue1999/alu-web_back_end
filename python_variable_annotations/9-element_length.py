#!/usr/bin/env python3
"""
This module contains a function to compute the length of elements in an iterable sequence.
"""

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, where each tuple contains an element from the iterable 
    and its corresponding length.
    
    Args:
        lst (Iterable[Sequence]): An iterable containing sequences.
        
    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, each containing a sequence 
        and its length.
    """
    return [(i, len(i)) for i in lst]
