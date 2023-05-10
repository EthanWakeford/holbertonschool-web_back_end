#!/usr/bin/env python3
"""async couroutieneslnsdrs"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """runs wait_random n number of times and return list of delays"""
    delays: List[float] = []

    for future in asyncio.as_completed(
            [wait_random(max_delay) for i in range(n)]):

        delays.append(await future)

    return delays
