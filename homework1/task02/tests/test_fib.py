from typing import List

import pytest
from fibonacci.fibonacci import check_fibonacci


@pytest.mark.parametrize(
    "lst",
    [
        [0],
        [0, 1],
        [0, 1, 1],
        [0, 1, 1, 2],
    ],
)
def test_fib(lst: List[int]):
    assert check_fibonacci(lst)


@pytest.mark.parametrize(
    "lst",
    [
        [],
        [5],
        [0, 3],
        [2, 4, 6],
        [0, 1, 1, 7],
    ],
)
def test_not_fib(
    lst: List[int],
):
    assert not check_fibonacci(lst)
