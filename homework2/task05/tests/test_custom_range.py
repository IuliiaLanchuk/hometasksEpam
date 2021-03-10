import string
from typing import Sequence

import pytest
from project5.task5 import custom_range


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [
        ((string.ascii_lowercase, "d"), ["a", "b", "c"]),
        ((string.ascii_lowercase, "c", "f"), ["c", "d", "e"]),
        ((string.ascii_lowercase, "p", "g", -2), ["p", "n", "l", "j", "h"]),
        (([1, 2, "abc", 4], 2, 4), [2, "abc"]),
        (([0, 1, 2, 3, 4, 5, 6], 3), [0, 1, 2]),
        (("01234567", "2", "5"), ["2", "3", "4"]),
    ],
)
def test_custom_range(value: Sequence, expected_result: Sequence):
    assert custom_range(*value) == expected_result
