"""
This module implements Merge Sort for sorting arrays of integers or floats.
"""

import rand

def merge_sort(input_arr):
    """
    Sorts an array using the Merge Sort algorithm.

    Args:
        arr (list): A list of integers or floats.

    Returns:
        list: A sorted list.
    """
    if not all(isinstance(x, (int, float)) for x in input_arr):
        raise ValueError("Input array must contain only integers or floats")
    if len(input_arr) <= 1:
        return input_arr

    half = len(input_arr) // 2
    return recombine(merge_sort(input_arr[:half]), merge_sort(input_arr[half:]))

def recombine(left_arr, right_arr):
    """
    Merges two sorted lists into a single sorted list.

    Args:
        left_arr (list): The left half of the sorted list.
        right_arr (list): The right half of the sorted list.

    Returns:
        list: A merged and sorted list.
    """
    left_index = 0
    right_index = 0
    merged_arr = [None] * (len(left_arr) + len(right_arr))

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merged_arr[left_index + right_index] = left_arr[left_index]
            left_index += 1
        else:
            merged_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1

    # Correctly appending remaining elements using `while` loops instead of `for`
    while left_index < len(left_arr):
        merged_arr[left_index + right_index] = left_arr[left_index]
        left_index += 1

    while right_index < len(right_arr):
        merged_arr[left_index + right_index] = right_arr[right_index]
        right_index += 1

    return merged_arr

# Generate a random array for testing
RANDOM_ARRAY = rand.random_array([None] * 20)
SORTED_ARRAY = merge_sort(RANDOM_ARRAY)

print(SORTED_ARRAY)
