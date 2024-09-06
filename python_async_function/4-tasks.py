#!/usr/bin/env python3
"""
This module defines the `task_wait_n` function that schedules
multiple coroutines using asyncio tasks.
"""

import asyncio
from typing import List
from importlib import import_module

# Import task_wait_random from '3-tasks'
tasks_module = import_module('3-tasks')
task_wait_random = tasks_module.task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay.
    Returns the list of delays in ascending order.
    Args:
        n (int): The number of coroutines to spawn.
        max_delay (int): The maximum delay for each coroutine.
    Returns:
        List[float]: A list of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
