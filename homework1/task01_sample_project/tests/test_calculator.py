"""
This is test_calculator.py docstring.

Here are tests for check_power_of_2 function
"""

import pytest
from calculator.calc import check_power_of_2


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [
        (65536, True),
        (12, False),
        (8, True),
        (3, False),
        (0, False),
        (4, True),
        (1 / 8, False),
    ],
)
def test_power_of_2(value: int, expected_result: bool):
    assert check_power_of_2(value) == expected_result
