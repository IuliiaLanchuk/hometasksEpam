from typing import Callable
from unittest.mock import Mock, call

import pytest
from project4.task4 import cache


def function(a: int, b: int) -> int:
    """Return result of math operation on arguments."""
    return pow(pow(a, b), 2)


@pytest.mark.parametrize(
    "func",
    [
        sum,
        pow,
        function,
    ],
)
def test_cache_same_values(func: Callable):
    some = [2, 4, 7]
    mock_func = Mock(func)
    cache_calc_sum_of_values = cache(mock_func)

    cache_calc_sum_of_values(*some)
    cache_calc_sum_of_values(*some)

    mock_func.assert_called_once()

    actual_result = mock_func.mock_calls
    assert actual_result == [call((2, 4, 7))]


@pytest.mark.parametrize(
    "func",
    [
        sum,
        pow,
        function,
    ],
)
def test_cache_different_values(func: Callable):
    func = Mock(func)
    cache_calc_sum_of_values = cache(func)

    cache_calc_sum_of_values(2, 4, 7)
    cache_calc_sum_of_values(2, 4, 8)

    assert func.call_count == 2

    actual_result = func.mock_calls
    assert actual_result == [call((2, 4, 7)), call((2, 4, 8))]
