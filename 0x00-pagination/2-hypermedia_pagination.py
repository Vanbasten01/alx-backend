#!/usr/bin/env python3
"""Simple pagination"""
import csv
import math
from typing import List, Dict, Any

index_range = __import__("0-simple_helper_function").index_range


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
        """Paginates the dataset and returns the specified
        page with a given page size."""
        assert isinstance(page, int) and page >= 1
        assert isinstance(page_size, int) and page_size >= 1
        start_index, end_index = index_range(page, page_size)
        try:
            return self.dataset()[start_index:end_index]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Returns paginated data along with metadata."""
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page + 1 < total_pages else None,
            "prev_page": page - 1 if page - 1 >= 1 else None,
            "total_pages": total_pages
        }
