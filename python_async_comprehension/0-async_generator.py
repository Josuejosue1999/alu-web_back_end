#!/usr/bin/env python3
"""
This module defines an asynchronous generator function `async_generator`
that yields random numbers between 0 and 10, with a 1-second delay per yield.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[int, None]:
    """
    Asynchronous generator that yields a random number between 0 and 10
    every 1 second, for a total of 10 times.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Wait for 1 second asynchronously
        yield random.randint(0, 10)  # Yield a random number between 0 and 10
