#!/usr/bin/env python3
"""
This module contains a function `make_multiplier` 
that returns a function
which multiplies a float by a specified multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float 
    by the specified multiplier.
    Args:
        multiplier (float): The multiplier to be used.
    Returns:
        Callable[[float], float]: A function that 
        multiplies a float by the multiplier.
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function
