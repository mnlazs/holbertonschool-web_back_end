#!/usr/bin/env python3
"""TASK PAGINATION"""
import csv
import math
from typing import List, Dict

def index_range(page, page_size):
    """Este módulo proporciona la funcionalidad
    de paginación de un conjunto de datos de nombres de bebés populares.
    """
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
        """definicion de la funcion get_page"""
        assert isinstance(
            page, int) and page > 0, "'page' tiene que ser un entero > que '0'"
        assert isinstance(
            page_size, int) and page_size > 0, "'page_size' must be > que '0'"
        inicio, fin = index_range(page, page_size)
        pages = []
        if inicio >= len(self.dataset()):
            return pages
        pages = self.dataset()
        return pages[inicio:fin]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[list]:
        """definicion de la funcion get_hyper"""
        total_pages = math.ceil(len(self.dataset) / page_size)
        
        if page_number > total_pages:
            page_number = total_pages
        
        page = self.get_page(page)
        
        next_page = page_number + 1 if page_number < total_pages else None
        prev_page = page_number - 1 if page_number > 1 else None
        
        return {
            'page_size': self.page_size,
            'page': page_number,
            'data': page,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }