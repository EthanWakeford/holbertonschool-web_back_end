#!/usr/bin/env python3
"""strongly typed"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiples multiplier by a float"""
    return lambda i: multiplier * i
