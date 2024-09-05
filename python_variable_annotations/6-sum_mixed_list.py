#!/usr/bin/env python3
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    list of integers and floats and returns their sum as a float.
    Args:
    mxd_lst (List[Union[int, float]]):
    Returns:
        float: The sum of the integers and floating-point numbers in the list.
    """
    return float(sum(mxd_lst))
