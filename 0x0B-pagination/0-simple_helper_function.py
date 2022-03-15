#!/usr/bin/env python3
"""
function that takes two integer arguments and return a
tuple of size two containing a start index and an end
index corresponding to the range of indexes to return
in a list for those particular pagination parameters
"""

from typing import Tuple


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
