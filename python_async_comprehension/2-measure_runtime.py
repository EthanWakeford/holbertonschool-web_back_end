#!/usr/bin/env python3
"""measures the runtime of running async function 4 times"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measures the run time"""
    t1 = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for i in range(4)])
    t2 = time.perf_counter()
    return t2 - t1
