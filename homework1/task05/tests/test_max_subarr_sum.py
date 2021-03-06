import sys

import pytest
from max_subarr_sum.task05 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ("a", "k", "expected_result"),
    [
        ([1, 3, -1, -3, 5], 2, 4),
        ([], 5, -sys.maxsize),
        ([1, 3], 0, 0),
        ([-1, -3, -1, -3, -5], 2, -4),
    ],
)
def test_max_subarr_sum(a: list[int], k: int, expected_result: int):
    assert find_maximal_subarray_sum(a, k) == expected_result
