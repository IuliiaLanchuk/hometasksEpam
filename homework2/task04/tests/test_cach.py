from typing import Callable, Tuple

import pytest
from project4.task4 import cache


def function(a: int, b: int) -> int:
    """Return result of math operation on arguments."""
    return (a ** b) ** 2


some = [1, 2]


def test_func_positive():
    cache_function = cache(function)
    assert cache_function(*some) is cache_function(*some)


def test_func_negative():
    cache_function = cache(function)
    assert cache_function(1, 2) is not cache_function(2, 1)


def test_sum():
    def summa(*args) -> int:
        return sum(args)

    cache_function = cache(summa)
    data = [1, 2]
    assert cache_function(*data) is cache_function(*data)


@pytest.mark.parametrize(
    ("func", "data", "expected_result"),
    [
        ((lambda x, y: x ** y ** 2), (2, 4), True),
        ((lambda x, y: x + y), [1, 2], True),
    ],
)
def test_cache(func: Callable, data: Tuple[int], expected_result: bool):
    temp_result = cache(func)
    assert (temp_result(*data) is temp_result(*data)) == expected_result
