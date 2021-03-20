"""
Task.

Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.
Write a detailed instruction how to run doctests**.

That how first steps for the instruction may look like:
 - Install Python 3.8 (https://www.python.org/downloads/)
 - Install pytest `pip install pytest`
 - Clone the repository <path your repository>
 - Checkout branch <your branch>
 - Open terminal
 - ...


Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - instructions how to run doctest with the pytest are provided

You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
 - how to write instructions

* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!"
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """Returns n FizzBuzz numbers. Any number divisible by three is replaced by the word fizz and any number
    divisible by five by the word buzz. Numbers divisible by 15 become fizz buzz.

    Doctests:
    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']
    >>> fizzbuzz('a')
    Traceback (most recent call last):
    ValueError: Input error. Required positive number
    >>> fizzbuzz(-1)
    Traceback (most recent call last):
    ValueError: Input error. Required positive number

    Detailed instruction how to run doctests:
    - Install Python 3.9 (https://www.python.org/downloads/)
    - Install pytest `pip install pytest`
    - Clone the repository <path your repository>.
    - In termonal run command <pytest path_to_file>.
    (for example, pytest F:/Iuliia/hometasksEpam/homework4/task4/task4_doctests.py)
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input error. Required positive number")
    else:
        return [
            "fizz buzz" * (i % 15 == 0)
            or "fizz" * (i % 3 == 0)
            or "buzz" * (i % 5 == 0)
            or str(i)
            for i in range(1, n + 1)
        ]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
