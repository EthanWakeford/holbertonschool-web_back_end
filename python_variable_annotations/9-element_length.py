#!/usr/bin/env python3
"""strongly typed"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns a list with a tuple containing the len and list of each item in
     iterable"""
    return [(i, len(i)) for i in lst]
