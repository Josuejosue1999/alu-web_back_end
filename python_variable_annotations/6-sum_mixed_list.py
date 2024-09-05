#!/usr/bin/env python3
"""
This module provides a function `sum_mixed_list` that takes a list of
integers and floats and returns their sum as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes a list of integers and floats, and returns their sum as a float.
    Args:
        mxd_lst (List[Union[int, float]]): A list containing integers and/or floats.
    Returns:
        float: The sum of the integers and floating-point numbers in the list.
    """
    return float(sum(mxd_lst))
