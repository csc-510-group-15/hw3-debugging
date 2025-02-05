"""
Unit tests for the bubble_sort function.
"""
from bubble_sort import bubble_sort

def test_sorted_lists():
    """Test sorting already-sorted lists."""
    input_sorted = [ 1, 2, 3, 5, 8, 13, 21, 34 ]
    assert bubble_sort(input_sorted) == input_sorted


def test_unsorted_lists():
    """Test sorting unsorted lists."""
    input_sorted = [ 1, 2, 3, 4, 5 ]
    input_unsorted = [ 3, 4, 2, 5, 1 ]
    assert bubble_sort(input_unsorted) == input_sorted
    input_reversed = [ 5, 4, 3, 2, 1 ]
    assert bubble_sort(input_reversed) == input_sorted


def test_empty_list():
    """Test sorting an empty list."""
    input_empty = [ ]
    assert bubble_sort(input_empty) == input_empty
    input_just_one = [ 1 ]
    assert bubble_sort(input_just_one) == input_just_one
    