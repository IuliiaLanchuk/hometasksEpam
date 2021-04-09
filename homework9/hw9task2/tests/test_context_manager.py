import pytest
from iterators_2.context_manager import SuppressorClass, suppressor_generator


def test_suppressor_as_generator_index_error_positive():
    with suppressor_generator(IndexError):
        ["a", "b", "c"][4]


def test_suppressor_as_generator_suppress_value_error_but_we_have_index_error_positive():
    with pytest.raises(IndexError):
        with suppressor_generator(ValueError):
            ["a", "b", "c"][4]


@pytest.mark.xfail
def test_suppressor_as_generator_suppress_index_error_and_we_have_also_index_error_negative():
    with pytest.raises(IndexError):
        with suppressor_generator(IndexError):
            [][0]


def test_suppressor_as_class_index_error_positive():
    with SuppressorClass(IndexError):
        [][2]


def test_suppressor_as_class_index_error_negative():
    with pytest.raises(IndexError):
        with SuppressorClass(ValueError):
            [][2]


def test_suppressor_as_class_zero_division_error_positive():
    with SuppressorClass(ZeroDivisionError):
        1 / 0


def test_suppressor_as_class_zero_division_error_negative():
    with pytest.raises(ZeroDivisionError):
        with SuppressorClass(ValueError):
            1 / 0


def test_suppressor_as_generator_value_error_positive():
    with suppressor_generator(ValueError):
        int("false")
