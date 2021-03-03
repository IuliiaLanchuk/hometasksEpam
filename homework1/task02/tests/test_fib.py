"""
This is test_fib.py docstring.

Here are tests for check_fibonacci function
"""

from typing import List

import pytest
from fibonacci.fibonacci import check_fibonacci


@pytest.mark.parametrize(
    ("lst", "expected_result"),
    [
        (
            [
                0,
                1,
                1,
                2,
                3,
                5,
                8,
                13,
                21,
                34,
                55,
                89,
                144,
                233,
                377,
                610,
                987,
                1597,
                2584,
                4181,
                6765,
            ],
            True,
        ),
        ([], False),
        ([0, 1, 1, 2, 3, 5, 7, 13, 21, 34, 54, 89, 144], False),
        ([0, 1], False),
    ],
)
def test_fibonacci(lst: List[int], expected_result: bool):
    actual_result = check_fibonacci(lst)

    assert actual_result == expected_result, "Invalid data"
