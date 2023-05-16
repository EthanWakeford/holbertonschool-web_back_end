#!/usr/bin/env python3
"""pagingiasndgiasngd"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    end: int = (page * page_size)
    return (end - page_size, end)
