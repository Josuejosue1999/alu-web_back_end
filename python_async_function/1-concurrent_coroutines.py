#!/usr/bin/env python3
"""
This module contains an asynchronous function `wait_n` that spawns the
`wait_random` coroutine multiple times and returns
the list of delays in ascending order.
"""

import asyncio
from typing import List
import importlib

# Import the `wait_random` function from the `0-basic_async_syntax.py` module
basic_async_syntax = importlib.import_module('0-basic_async_syntax')
wait_random = basic_async_syntax.wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously spawns `wait_random` n times with
    the specified max_delay
    and returns a list of all the delays in ascending order without using sort().
    
    Args:
    n (int): The number of times to spawn `wait_random`.
        max_delay (int): The maximum delay for `wait_random`.
    
    Returns:
        List[float]: A list of delays in ascending order.
    """
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        # Insertion sort mechanism to maintain ascending order
        if not delays or delay >= delays[-1]:
            delays.append(delay)
        else:
            for i in range(len(delays)):
                if delay < delays[i]:
                    delays.insert(i, delay)
                    break
    return delays
