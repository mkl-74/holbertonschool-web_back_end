#!/usr/bin/env python3
"""
Implement a get_hyper method that takes the same arguments (and defaults
as get_page and returns a dictionary containing
the following key-value pairs
"""

import csv
import math
from typing import List, Dict, Union


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Returns a tuple of start index and end index for a given page and page size.  # noqa
    """
    # Calculate the start index
    start_index = (page - 1) * page_size

    # Calculate the end index
    end_index = start_index + page_size

    return start_index, end_index


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
        """
        Retrieves a specific page of data from the dataset.
        """
        # Validate input arguments
        assert isinstance(page, int) and page > 0, "Page must be a positive integer"  # noqa
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer"  # noqa

        # Get the start and end index for the page
        start_index, end_index = index_range(page, page_size)

        # Get the dataset
        dataset = self.dataset()

        # Slice the dataset based on the start and end index
        page_data = dataset[start_index:end_index]

        return page_data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Union[int, List[List], None]]:  # noqa
        """
        Retrieves a specific page of data from the dataset with hypermedia information.  # noqa
        """
        # Get the page data using get_page method
        page_data = self.get_page(page, page_size)

        # Calculate total number of pages
        total_pages = math.ceil(len(self.dataset()) / page_size)

        # Calculate next page number
        next_page = page + 1 if page < total_pages else None

        # Calculate previous page number
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(page_data),
            "page": page,
            "data": page_data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
