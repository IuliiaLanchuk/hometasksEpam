"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any, Iterable, Iterator, Mapping

occurrences = 0


def recursively_read(tree: Iterable, element) -> int:
    global occurrences
    iterator: Iterator
    if isinstance(tree, Mapping):
        iterator = iter(tree.values())
    else:
        iterator = iter(tree)
    while True:
        next_element = next(iterator, None)
        if isinstance(next_element, Iterable) and not isinstance(
            next_element, (str, bytes, bytearray)
        ):
            recursively_read(next_element, element)
        if next_element == element:
            occurrences += 1
        if next_element is None:
            break

    return occurrences


def find_occurrences(tree: dict, element: Any) -> int:
    global occurrences
    occurrences = 0
    return recursively_read(tree, element)
