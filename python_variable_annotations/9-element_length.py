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
    Returns a list of tuples, where each tuple contains an element from the iterable 
    and its corresponding length.
    
    Args:
        lst (Iterable[Sequence]): An iterable containing sequences.
        
    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, each containing a sequence 
        and its length.
    """
    return [(i, len(i)) for i in lst]
