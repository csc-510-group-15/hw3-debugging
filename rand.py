"""
This module provides functions for generating random numbers.
"""

import random

def random_array(arr):
    """
    Populates an array with random integers between 1 and 20.

    Args:
        arr (list): A list with placeholder values.

    Returns:
        list: A list of randomly generated integers.
    """
    return [random.randint(1, 20) for _ in arr]
