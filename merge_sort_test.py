"""
Unit tests for the merge_sort function.
"""
import pytest
from hw2_debugging import merge_sort

def test_single_element():
    """Test sorting a single-element list."""
    input_arr = [42]
    assert merge_sort(input_arr) == [42]

def test_large_numbers():
    """Test sorting a list with large integer values."""
    input_arr = [99999999, 123456, 987654321, 1111, 500000]
    assert merge_sort(input_arr) == [1111, 123456, 500000, 99999999, 987654321]

def test_invalid_input():
    """Test that invalid input (non-numeric values) raises a ValueError."""
    input_arr = [1, "two", 3.5]
    with pytest.raises(ValueError):
        merge_sort(input_arr)
