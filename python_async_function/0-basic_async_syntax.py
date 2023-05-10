#!/usr/bin/env python3
"""async coroutine"""
import asyncio
import random


async def wait_random(max_delay: int=10) -> float:
    """waits a random amount of time before returning"""
    delay: float = random.random()
    await asyncio.sleep(delay)
    return delay
