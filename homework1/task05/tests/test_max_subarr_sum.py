"""
This is test_max_subarr_sum.py docstring.

Here are tests for check_sum_of_four function
"""


import pytest
from max_subarr_sum.task05 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ("a", "k", "expected_result"),
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([6, 1, 3, -1, -3, 1, 17, 5, 3, 6, 7], 2, 22),
        ([], 5, 0),
        (
            [
                6,
                1,
                3,
                -1,
                -3,
                -4,
                29,
                5,
                3,
                0,
                7,
                6,
                1,
                3,
                -1,
                1,
                3,
                -1,
                -3,
                -4,
                -3,
                1,
                13,
                5,
                3,
                6,
                7,
                1,
                3,
                -1,
                -3,
                -4,
                23,
                0,
                -15,
            ],
            7,
            51,
        ),
        ([1, 3, -1, -3, 5, 3, 6, 7], 0, 0),
        ([1, 3, -1, -3, 5, 3, 6, 7], -2, 0),
    ],
)
def test_max_subarr_sum(a: list[int], k: int, expected_result: int):
    actual_result = find_maximal_subarray_sum(a, k)

    assert actual_result == expected_result
