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

    def wrapper(func: Callable) -> Any:
        current_time = 0
        cash_data = None

        def wrapped(*args: int, **kwargs: int) -> Any:
            nonlocal current_time, cash_data
            if current_time > 0:
                current_time -= 1
                return cash_data
            else:
                cash_data = func(*args, **kwargs)
                current_time = times
                return cash_data

        return wrapped

    return wrapper
