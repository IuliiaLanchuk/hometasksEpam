"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any, Iterable, Iterator, Mapping


def recursively_read(tree: Iterable, element, occurrences: list):
    iterator: Iterator
    if isinstance(tree, Mapping):
        iterator = iter(tree.values())
    else:
        iterator = iter(tree)
    while True:
        try:
            next_element = next(iterator)
            if isinstance(next_element, Iterable) and not isinstance(
                next_element, (str, bytes, bytearray)
            ):
                recursively_read(next_element, element, occurrences)
            if next_element == element:
                occurrences[0] += 1
        except StopIteration:
            break

    return occurrences[0]


def find_occurrences(tree: dict, element: Any) -> int:
    return recursively_read(tree, element, [0])
