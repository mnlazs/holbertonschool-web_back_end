#!/usr/bin/env python3
import csv
import math
from typing import List
"""copy funcion index_range"""


def index_range(page, page_size):
    """return una tupla"""
    if page and page_size:
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return (start_index, end_index)


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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(
            page, int) and page > 0, "Argumento 'page' tiene que ser un entero mayor que '0'"
        assert isinstance(
            page_size, int) and page_size > 0, "Argumento 'page_size' tiene que se mayor que '0'"
        inicio, fin = index_range(page, page_size)
        pages = []
        if inicio >= len(self.dataset()):
            return pages
        pages = self.dataset()
        return pages[inicio:fin]
