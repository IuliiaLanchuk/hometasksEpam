"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from typing import Callable


def function(a: int, b: int) -> int:
    """Return result of math operation on arguments."""
    return (a ** b) ** 2


def multiply(a: int, b: int) -> int:
    """Return result of arguments sum."""
    return a + b


def operations(a: int, b: int) -> int:
    """Return result of math operation on arguments."""
    return (a + b) // 2


def cache(func: Callable) -> Callable:
    """Return function."""
    cache_data = {}

    def wrapper(*args: int) -> int:
        """Return cache data."""
        if args not in cache_data:
            cache_data[args] = func(*args)
        return cache_data[args]

    return wrapper
