"""
Task.

In previous homework 2 task 4, you wrote a cache function that remembers other function output value.
Modify it to be a parametrized decorator, so that the following code:

@cache(times=3)
def some_function():
    pass
Would give out cached value up to times number only. Example:

@cache(times=2)
def f():
    return input('? ')   # careful with input() in python2, use raw_input() instead

f()
? 1
'1'
f()     # will remember previous value
'1'
f()     # but use it up to two times only
'1'
f()
? 2
'2'
"""
from typing import Any, Callable


def cache(times: int) -> Callable:
    """
    Remember other function output value. Give out cached value up to times number.

    :times: quantity of returned cached values
    """

    def wrapper(func: Callable) -> Callable:
        cache_data = {}
        if times < 1:
            raise ValueError("Times value should be more than zero")

        def timer(*args: Any) -> Any:
            if args in cache_data and cache_data[args][1] < times:
                cache_data[args][1] += 1
                return cache_data[args][0]
            else:
                func_output_value = func(*args)
                cache_data[args] = [func_output_value, 0]
                return func_output_value

        return timer

    return wrapper
