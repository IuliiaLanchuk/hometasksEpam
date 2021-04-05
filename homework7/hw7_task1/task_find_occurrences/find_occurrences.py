"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any, Iterable, Mapping


def recursively_read(tree: Iterable, element) -> int:
    occurrences = 0
    if isinstance(tree, Mapping):
        iterator = iter(tree.values())
    else:
        iterator = iter(tree)

    sentinel = object()
    while (next_element := next(iterator, sentinel)) != sentinel:
        if isinstance(next_element, Iterable) and not isinstance(
            next_element, (str, bytes, bytearray)
        ):
            occurrences += recursively_read(next_element, element)
        if next_element == element:
            occurrences += 1

    return occurrences


def find_occurrences(tree: dict, element: Any) -> int:
    return recursively_read(tree, element)
