import pytest
from project1.task1 import cache


@cache(times=2)
def f(a: int):
    return a + 1


def test_cache_decorator():
    assert f(6) is f() is f()


def test_cache_decorator_error():
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'a'"):
        assert f(3) is f() is f() is f()
