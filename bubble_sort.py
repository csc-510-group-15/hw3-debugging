"""
This module implements a Bubble Sort algorithm for debugging practice.
"""

def bubble_sort(elements: list):
    """
    Performs a Bubble Sort on the given list of elements.

    Args:
        elements (list): A list of elements to sort.

    Returns:
        list: The sorted list of elements.
    """

    sorted_elements = elements.copy()
    count = len(sorted_elements)

    for i in range(count):
        swapped = False

        for j in range(0, count - i - 1):
            if sorted_elements[j] > sorted_elements[j + 1]:
                sorted_elements[j], sorted_elements[j + 1] = sorted_elements[j + 1], sorted_elements[j]
                swapped = True

        if not swapped:
            break

    return sorted_elements

test_list = [ 1, 2, 3, 4, 5 ]
test_list_2 = [ 5, 4, 3, 2, 1 ]
test_list_3 = [ 3, 4, 2, 5, 1 ]

print(bubble_sort(test_list))
print(bubble_sort(test_list_2))
print(bubble_sort(test_list_3))
