from unittest.mock import Mock, call

from project4.task4 import cache


def function(a: int, b: int) -> int:
    """Return result of math operation on arguments."""
    return pow(pow(a, b), 2)


def test_cache_same_values_func_called_ones():
    some = [2, 4, 7]
    mock_func = Mock()
    cache_calc_sum_of_values = cache(mock_func)

    cache_calc_sum_of_values(*some)
    cache_calc_sum_of_values(*some)

    mock_func.assert_called_once()
    assert mock_func.mock_calls == [call((2, 4, 7))]


def test_cache_different_values_func_called_several_times():
    func = Mock()
    cache_calc_sum_of_values = cache(func)

    cache_calc_sum_of_values(2, 4, 7)
    cache_calc_sum_of_values(2, 4, 8)

    assert func.call_count == 2
    assert func.mock_calls == [call((2, 4, 7)), call((2, 4, 8))]


def test_cache_sum():
    some = [1, 2]
    cache_calc_sum_of_values = cache(sum)
    assert cache_calc_sum_of_values(*some) == cache_calc_sum_of_values(*some)


def test_cache_sum_reversed_args():
    cache_function = cache(sum)
    assert cache_function(1, 2) is not cache_function(2, 1)
