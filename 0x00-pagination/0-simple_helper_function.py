#!/usr/bin/env python3
"""
This module provides a function for calculating the start and end indices
for a specified page and page size.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    """
    Calculate the start and end indices for a specified page and page size.

    Args:
    - page (int): The page number.
    - page_size (int): The size of each page.

    Returns:
    - Tuple[int]: A tuple containing the start and end indices.
    """
    start_index = 0
    end_index = 0
    for i in range(page):
        if i >= 1:
            start_index += page_size
        end_index = start_index + page_size
    return (start_index, end_index)
