"""
Task02.

Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""

from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    """
    Return True if sequence is a fibonacci sequence.

    :param data: input list of integers
    :return: bool
    """
    counter = 2
    if data == [0] or data == [0, 1]:
        return True
    if len(data) > 2:
        for i in range(2, len(data)):
            if data[i] == data[i - 2] + data[i - 1]:
                counter += 1

    return counter == len(data) != 2 and data[0] == 0
