#!/usr/bin/env python3
"""has an async generator"""
import asyncio
import random


async def async_generator() -> float:
    """yields random number with awaiting sleep 1 second"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
    return
