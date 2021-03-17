"""
This task is optional.

Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the implementation in this video**.


Definition of done:
 - function is created
 - function is properly formatted
 - function has tests


#>>> list(fizzbuzz(5))
["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""
from typing import Generator


def fizzbuzz(n: int) -> Generator:
    """Return a generator that yields n FizzBuzz numbers."""

    def fizz_buzz_generation(x: int) -> str:
        """Return "fizz" if x is divided by 3 or "buzz" if x id divided by 5 or
        "fizz buzz" if x is divided by 15 or x."""
        return (
            "fizz buzz" * (x % 15 == 0)
            or "fizz" * (x % 3 == 0)
            or "buzz" * (x % 5 == 0)
            or str(x)
        )

    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input error. Required positive number")
    else:
        for i in map(fizz_buzz_generation, range(1, n + 1)):
            yield i
