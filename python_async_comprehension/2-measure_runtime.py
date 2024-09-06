#!/usr/bin/env python3
"""
This module defines a coroutine `measure_runtime` that measures the
total runtime of executing `async_comprehension` four times in parallel
using asyncio.gather.
"""

import asyncio
import time
import importlib.util
import sys

# Dynamically load the module
module_name = '1-async_comprehension'
module_path = f'./{module_name}.py'
spec = importlib.util.spec_from_file_location(module_name, module_path)
async_comprehension_module = importlib.util.module_from_spec(spec)
sys.modules[module_name] = async_comprehension_module
spec.loader.exec_module(async_comprehension_module)

# Import the function
async_comprehension = async_comprehension_module.async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime of executing `async_comprehension`
    four times in parallel using asyncio.gather.
    Returns:
        float: The total runtime for the four executions.
    """
    start_time = time.time()  # Record the start time

    # Execute `async_comprehension` four times in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.time()  # Record the end time
    total_time = end_time - start_time  # Calculate the total runtime
    return total_time
