"""
This is test_sum_of_four.py docstring.

Here are tests for check_sum_of_four function
"""


import pytest
from sum_of_four.task04 import check_sum_of_four


@pytest.mark.parametrize(
    ("a", "b", "c", "d", "expected_result"),
    [
        (
            [1, -2, 3, 4, -5],
            [6, 7, 2, 9, 5],
            [-10, 12, -13, 14, 15],
            [16, 17, 13, 19, 20],
            4,
        ),
        (
            [1, -2, 3, 4, 5],
            [6, 7, 2, 9, 5],
            [-10, 12, -13, 14, 15],
            [16, 17, 13, 19, 20],
            1,
        ),
        (
            [1, 2, 3, 4, 5],
            [6, 7, 2, 9, 5],
            [10, 12, 13, 14, 15],
            [16, 17, 13, 19, 20],
            0,
        ),
        (
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [11, 12, 13, 14, 15, 16, 17, 18, 19],
            [-1, -2, -3, -4, -5, -6, -7, -8, -9],
            [-11, -12, -13, -14, -15, -16, -17, -18, -19],
            489,
        ),
        ([1], [1], [-1], [-1], 1),
    ],
)
def test_sum_of_four(
    a: list[int], b: list[int], c: list[int], d: list[int], expected_result: tuple
):
    actual_result = check_sum_of_four(a, b, c, d)

    assert actual_result == expected_result
