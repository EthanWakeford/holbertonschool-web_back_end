#!/usr/bin/env python3
"""collects and returns 10 random numbers using async generator"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """uses an async comprehesion to create a list of random numbers"""
    return [i async for i in async_generator()]
