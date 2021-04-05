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
from typing import Any, Callable


def cache(func: Callable) -> Callable:
    """Return function."""
    cache_data = {}

    def wrapper(*args: Any) -> Any:
        """Return cache data."""
        str_args = str(args)
        if str_args not in cache_data:
            cache_data[str_args] = func(*args)
        return args, cache_data.get(str_args)

    return wrapper
