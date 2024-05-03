#!/usr/bin/env python3
"""function named index_range that takes two
integer arguments page and page_size"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Returns a tuple of start index and end index for a
    given page and page size.
    """
    # Calculate the start index
    start_index = (page - 1) * page_size

    # Calculate the end index
    end_index = start_index + page_size

    return start_index, end_index


# Test cases
if __name__ == "__main__":
    res = index_range(1, 7)
    print(type(res))
    print(res)

    res = index_range(page=3, page_size=15)
    print(type(res))
    print(res)
