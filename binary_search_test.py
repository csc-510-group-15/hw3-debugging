"""
Unit tests for the binary_search function.
"""
from binary_search import binary_search

def test_valid_targets():
    """Test searching for values that exist in the list."""
    input_standard = [ 1, 2, 3, 5, 8, 13, 21, 34 ]
    for i in range(len(input_standard)):
        assert binary_search(input_standard, input_standard[i]) == i

    input_negatives = [ -34, -21, -13, -8, -5, -3, -2, -1 ]
    for i in range(len(input_negatives)):
        assert binary_search(input_negatives, input_negatives[i]) == i

    input_big_numbers = [0, 10000, 20000, 30000, 40000, 100000]
    for i in range(len(input_big_numbers)):
        assert binary_search(input_big_numbers, input_big_numbers[i]) == i


def test_invalid_targets():
    """Test searching for values that do not exist in the list."""
    test_list = [ 1, 3, 5, 7, 9, 11, 13, 15 ]
    for i in range(len(test_list)):
        assert binary_search(test_list, test_list[i] + 1) == -1