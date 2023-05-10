#!/usr/bin/env python3
"""strongly typed"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns sum of list"""
    return sum(mxd_lst)
