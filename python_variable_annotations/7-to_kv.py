#!/usr/bin/env python3
from typing import Tuple, Union

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This function takes a string k and an integer or float v,
    and returns a tuple where the first element is the string k,
    and the second element is the square of v as a float.

    Args:
        k (str): The string.
        v (Union[int, float]): The integer or floating-point number.

    Returns:
        Tuple[str, float]: A tuple where the first element is k and the second
                           element is the square of v as a float.
    """
    return (k, float(v ** 2))
