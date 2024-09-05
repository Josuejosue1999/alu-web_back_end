#!/usr/bin/env python3
"""
This module provides a function `sum_list` that calculates the sum of a
list of floating-point numbers.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    This function takes a list of floats and returns their sum.
    Args:
        input_list (List[float]): A list of floating-point numbers.
    Returns:
        float: The sum of the floating-point numbers in the list.
    """
    return sum(input_list)
