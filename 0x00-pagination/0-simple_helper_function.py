#!/usr/bin/env python3
""" This script has a helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """ Creates index Tuple of page"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
