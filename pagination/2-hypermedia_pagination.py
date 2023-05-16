#!/usr/bin/env python3
"""hyper paginationa"""
import csv
import math
from typing import List, Tuple, Dict, Union
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> Tuple[List[List], int]:  # noqa
        """gets a page from a csv file"""
        assert ((type(page) == int and page > 0) and (type(page_size) == int and page_size > 0))  # noqa
        range: Tuple[int, int] = index_range(page, page_size)

        with open('Popular_Baby_names.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            page: List[List] = []
            line_count: int = 0
            for row in csv_reader:
                if range[0] < line_count <= range[1]:
                    page.append(row)
                line_count += 1
            if range[1] > line_count:
                return ([], line_count)
            return (page, line_count)

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Union[int, str]]:  # noqa
        """gets real hyper"""
        data, rows = self.get_page(page, page_size)
        pages = rows // page_size
        if pages % page_size != 0:
            pages += 1

        hyper = {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': page + 1 if page + 1 <= pages else None,
            'prev_page': page - 1 if page >= 0 else None,
            'total_pages': pages
        }

        return hyper
