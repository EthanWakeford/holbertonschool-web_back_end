#!/usr/bin/env python3
"""async pythonon"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """runs wait_random n number of times and return list of delays"""
    delays: List[float] = []

    for future in asyncio.as_completed([task_wait_random(max_delay) for i in range(n)]):  # noqa
        delays.append(await future)

    return delays
