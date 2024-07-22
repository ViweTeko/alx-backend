#!/usr/bin/env python3
""" More addition to previous tasks"""
from typing import Dict, List, Tuple
import csv
import math


def index_range(page: int, page_size: int) -> Tuple:
    """Tuple containing start and end indices"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index


class Server:
    """Server class paginates database of popular baby names"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as file:
                reader = csv.reader(file)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Creates list of paginated data"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        a_index, z_index = index_range(page, page_size)
        dataset = self.dataset()
        if a_index > len(dataset) or z_index > len(dataset):
            return []
        return dataset[a_index: z_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Creates hypermedia Metadata pagination"""
        data = self.get_page(page, page_size)
        dataset = self.dataset()
        a_index, z_index = index_range(page, page_size)

        if page == 1:
            prev_page = None
        else:
            prev_page = - 1
        if z_index > len(dataset):
            next_page = None
        else:
            next_page = page + 1
        tot_pages = math.ceil(len(dataset) / page_size)

        return {
            'page': page,
            'page_size': page_size,
            'data': data,
            'prev_page': prev_page,
            'next_page': next_page,
            'tot_pages': tot_pages
        }
