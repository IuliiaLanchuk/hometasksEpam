from unittest.mock import Mock

import pytest
from project_cache.task1cache import cache


def test_cache_func_times_is_1_third_call_with_1_value_is_when_cache_was_already_cleared(
    capsys,
):
    @cache(times=1)
    def foo(arg):
        print(arg)
        return arg

    foo(1)
    foo(1)
    foo(2)
    foo(1)

    captured = capsys.readouterr()

    assert captured.out == "1\n2\n1\n"


def test_cache_func_times_is_2_with_6_value_after_4th_func_call_cache_was_cleared(
    capsys,
):
    @cache(times=2)
    def foo(arg):
        print(arg)
        return arg

    foo(6)
    foo(6)
    foo(6)
    foo(6)

    captured = capsys.readouterr()

    assert captured.out == "6\n6\n"


def test_cache_func_with_mock_after_4th_func_call_cache_was_cleared(capsys):
    @cache(times=3)
    def foo(*arg):
        return arg

    a, b, c, d, f = foo(Mock), foo(Mock), foo(Mock), foo(Mock), foo(Mock)

    assert a is b
    assert b is c
    assert c is d
    assert d is not f


def test_cache_with_0_times_exception():
    def func(arg):
        return arg

    with pytest.raises(ValueError, match="Times value should be more than zero"):
        cache(times=0)(func(9))
