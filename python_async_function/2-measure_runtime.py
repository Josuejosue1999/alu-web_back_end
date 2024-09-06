#!/usr/bin/env python3
"""
This module contains a function `measure_time` that measures the
execution time of the `wait_n` function and returns the average time per call.
"""

import time
import asyncio
import importlib

# Import dynamically the '1-concurrent_coroutines' module
concurrent_coroutines = importlib.import_module('1-concurrent_coroutines')
wait_n = concurrent_coroutines.wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total runtime of executing wait_n(n, max_delay)
    and return the average runtime per call.
    Args:
        n (int): The number of times to spawn wait_random
        via wait_n.
        max_delay (int): The maximum delay for wait_random.
    Returns:
        float: The average time per execution of wait_n.
    """
    start_time = time.time()  # Start measuring time
    # Execute the `wait_n` function using asyncio
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()  # End measuring time
    
    total_time = end_time - start_time  # Calculate total time
    return total_time / n  # Return the average time per execution
