from typing import List

import pytest
from fibonacci.fibonacci import check_fibonacci


@pytest.mark.parametrize(
    ("lst", "expected_result"),
    [
        (
            [0, 1, 1, 2, 3, 5, 8],
            True,
        ),
        ([], False),
        ([0, 1, 1, 2, 7], False),
        ([0, 1], True),
        ([2, 4, 6], False),
    ],
)
def test_fibonacci(lst: List[int], expected_result: bool):
    assert check_fibonacci(lst) == expected_result
