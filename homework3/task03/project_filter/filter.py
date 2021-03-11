"""Task.

The task is to write a code that generates data filtering object from a list of keyword parameters.
There are multiple bugs in this code. Find them all and write tests for faulty cases.
"""


class Filter:
    """
    Helper filter class. Accepts a list of single-argument
    functions that return True if object in list conforms to some criteria
    """

    def __init__(self, *functions):
        self.functions = functions

    def apply(self, data):
        return [item for item in data if all(i(item) for i in self.functions)]


def make_filter(**keywords):
    """
    Generate filter object for specified keywords
    """
    filter_funcs = []
    for key, value in keywords.items():

        def keyword_filter_func(data, key_=key, value_=value):
            return data[key_] == value_

        filter_funcs.append(keyword_filter_func)
    return Filter(*filter_funcs)
