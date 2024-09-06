#!/usr/bin/env python3
"""
This module defines a function `task_wait_random`
that creates an asyncio task for the wait_random coroutine.
"""

import asyncio
from importlib import import_module

# Import dynamically the 'wait_random' function from '0-basic_async_syntax'
basic_async_syntax = import_module('0-basic_async_syntax')
wait_random = basic_async_syntax.wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio task for the wait_random coroutine.
    Args:
        max_delay (int): The maximum delay for wait_random.
    Returns:
        asyncio.Task: An asyncio task for wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
