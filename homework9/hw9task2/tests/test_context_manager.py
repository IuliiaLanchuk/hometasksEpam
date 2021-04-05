import pytest
from iterators_2.context_manager import SuppressorClass, suppressor_generator


def test_suppressor_as_generator_index_error_positive():
    with suppressor_generator(IndexError):
        print(["a", "b", "c"][4])


def test_suppressor_as_generator_index_error_negative():
    with pytest.raises(IndexError):
        with suppressor_generator(ValueError):
            print(["a", "b", "c"][4])


def test_suppressor_as_class_index_error_positive():
    with SuppressorClass(IndexError):
        print([][2])


def test_suppressor_as_class_index_error_negative():
    with pytest.raises(IndexError):
        with SuppressorClass(ValueError):
            print([][2])


def test_suppressor_as_class_zero_division_error_positive():
    with SuppressorClass(ZeroDivisionError):
        print(1 / 0)


def test_suppressor_as_class_zero_division_error_negative():
    with pytest.raises(ZeroDivisionError):
        with SuppressorClass(ValueError):
            print(1 / 0)


def test_suppressor_as_generator_value_error_positive():
    with suppressor_generator(ValueError):
        print(int("false"))
