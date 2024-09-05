#!/usr/bin/env python3
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    returns a function that multiplies a float by this multiplier.
    Args:
        multiplier (float): The multiplier to be used.
    Returns:
        Callable[[float], float]:
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function
