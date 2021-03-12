import pytest
from project_is_armstrong.task4_armstrong import is_armstrong


@pytest.mark.parametrize("number", [153])
def test_is_armstrong_true(number: int):
    assert is_armstrong(number) is True, "Is Armstrong number"


@pytest.mark.parametrize("number", [10])
def test_is_armstrong_false(number: int):
    assert is_armstrong(number) is False, "Is not Armstrong number"
