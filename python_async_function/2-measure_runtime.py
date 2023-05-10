#!/usr/bin/env python3
"""async snakes"""
import asyncio
from time import perf_counter
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures the time to run wait_n"""
    start: float = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end: float = perf_counter()
    return end - start
