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
    fib1 = 0
    fib2 = 1
    fib3 = 1
    lst = [0, 1, 1]
    if len(data) > 0:
        if data == [0] or data == [0, 1] or data == [0, 1, 1]:
            return True
        else:
            while fib3 < data[-1]:
                fib1 = fib2
                fib2 = fib3
                fib3 = fib1 + fib2
                lst.append(fib3)
    return data == lst
