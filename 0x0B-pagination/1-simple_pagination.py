#!/usr/bin/env python3
"""
Find the correct indexes to paginate the dataset correctly and
return the appropriate page of the dataset
"""

import csv
import math
from typing import Tuple, List


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
        """Get the page
            Args:
                page - actual page
                page_size - size of the page
            Return:
                -List with pagination realized
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        range: Tuple = index_range(page, page_size)
        pagination: List = self.dataset()

        return (pagination[range[0]:range[1]])


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Range of a page
       Args:
           page: actual page
           page_size: size of the page
       return:
           Tuple with a start index and an end index
    """
    final_size = page * page_size
    start_size = final_size - page_size

    return (start_size, final_size)
