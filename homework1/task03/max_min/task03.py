"""
Task03.

Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.

For example for [1, 2, 3, 4, 5], function should return [1, 5]

We guarantee, that file exists and contains line-delimited integers.

To read file line-by-line you can use this snippet:

with open("some_file.txt") as fi:
    for line in fi:
        ...

"""


import sys
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    """
    I'm find min and max values in file.

    :param file_name: input file name
    :return: tuple of two values
    """
    max_value = 0
    min_value = sys.maxsize
    with open(file_name) as fi:
        for line in fi:
            if line != "\n":
                number = int(line.rstrip())
                if number > max_value:
                    max_value = number
                if number < min_value:
                    min_value = number
    return min_value, max_value
