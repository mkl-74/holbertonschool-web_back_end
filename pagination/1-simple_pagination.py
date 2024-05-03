#!/usr/bin/env python3
"""Copy index_range from the previous task and the following class into your code"""

import csv
from typing import List


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Returns a tuple of start index and end index for a given page and page size.
    """
    start_index = (page - 1) * page_size
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
        assert isinstance(page, int) and page > 0, "Page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer"

        # Get the start and end index for the page
        start_index, end_index = index_range(page, page_size)

        # Get the dataset
        dataset = self.dataset()

        # Slice the dataset based on the start and end index
        page_data = dataset[start_index:end_index]

        return page_data
