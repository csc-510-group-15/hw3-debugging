"""
This module implements a faulty Binary Search algorithm for debugging practice.
"""

def binary_search(elements: list, target):
    """
    Performs a Binary Search for a target value on a sorted list of elements.
    Behavior is undefined for unsorted lists.

    Args:
        elements (list): A sorted list of elements from which to locate the target.
        target: The value to find the index of in the elements list.

    Returns:
        list: The index in the list at which the target value is found, or -1 if it is not found.
    """

    # Set up pointers that will help us cut the possible locations in half at each iteration.
    low = 0
    high = len(elements) - 1

    # Iterate until every element has been eliminated from contention;
    # the search window is less than 1 element wide.
    while low <= high:
        # Check if the middle element of the search window is the value we're searching for.
        mid = (low + high) // 2

        if elements[mid] == target:
            # Exact match: return the index where we found the target.
            return mid

        if elements[mid] < target:
            # Middle element TOO LOW: use the higher half of the search window.
            low = mid + 1
        else:
            # Middle element TOO HIGH: use the lower half of the search window.
            high = mid - 1

    # Target value is not in the elements array; return an error value.
    return -1

# Example graph (Adjacency List Representation)
test_list = [ 1, 2, 3, 5, 8, 13, 21, 34 ]

# Run Binary Search on every element present in the test list.
print([binary_search(test_list, n) for n in test_list])
# Run Binary Search on some elements NOT present in the test list.
print(binary_search(test_list, -4))
print(binary_search(test_list, 4))
print(binary_search(test_list, 15))
print(binary_search(test_list, 150))
