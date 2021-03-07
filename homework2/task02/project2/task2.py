"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1

"""
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    """Return the most common and the least common elements from input sequence."""
    all_elements = {}
    max_element = ""
    min_element = ""
    for i in inp:
        if i in all_elements:
            all_elements[i] += 1
        else:
            all_elements[i] = 1
    max_amount = max(all_elements.values())
    min_amount = min(all_elements.values())

    for key, value in all_elements.items():
        if value == max_amount:
            max_element = int(key)
        if value == min_amount:
            min_element = int(key)
    return max_element, min_element
