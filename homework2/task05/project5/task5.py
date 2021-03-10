"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""


def custom_range(input_data, start, finish=None, step=1):
    """Return a list of values after slicing of input sequence."""
    result = []
    if start in input_data:
        if finish is None:
            finish = start
            start = input_data[0]
        for i in input_data[input_data.index(start) : input_data.index(finish) : step]:
            result.append(i)
    return result
