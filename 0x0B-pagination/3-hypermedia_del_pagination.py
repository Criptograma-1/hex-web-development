#!/usr/bin/env python3
"""
Make sure that if between two queries, certain rows are removed
from the dataset, the user does not miss items from dataset when changing page.
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""
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
        """Data set indexed by rank position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }

        return self.__indexed_dataset

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

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Get hyperindice
            Args:
                index - current page number
                page_size - the length of the page
            Return:
                Dict containing
                    -the current start index of the return page
                    -the next index to query with
                    -the current page size
                    -the actual page of the dataset
        """
        dataset_result = []
        index_data = self.indexed_dataset()
        keys_list = list(index_data.keys())
        assert index + page_size < len(keys_list)
        assert index < len(keys_list)

        if index not in index_data:
            start_index = keys_list[index]
        else:
            start_index = index

        for i in range(start_index, start_index + page_size):
            if i not in index_data:
                dataset_result.append(index_data[keys_list[i]])
            else:
                dataset_result.append(index_data[i])

        next_index = index + page_size

        if index in keys_list:
            next_index
        else:
            next_index = keys_list[next_index]

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(dataset_result),
            'data': dataset_result
        }
