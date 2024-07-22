#!/usr/bin/env python3
"""Deletion resilient hypermedia pagination"""
import csv
import math
from typing import Dict, List


class Server:
    """Server class that paginates popular baby names"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                a: dataset[a] for a in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        if not (0 <= index < len(self.indexed_dataset())):
            raise AssertionError("Index out of range")
        data = []
        curr_idx = index
        while len(data) < page_size and curr_idx < len(self.indexed_dataset()):
            try:
                curr_idx < len(self.indexed_dataset()[curr_idx])
                curr_idx += 1
            except KeyError:
                break
        next_idx = curr_idx
        return {
            'index': index,
            'next_idx': next_idx,
            'page_size': page_size,
            'data': data,
        }
