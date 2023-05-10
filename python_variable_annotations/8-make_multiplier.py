#!/usr/bin/env python3
"""strongly typed"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    return lambda i: multiplier * i
