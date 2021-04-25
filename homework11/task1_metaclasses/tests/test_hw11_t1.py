import pytest
from project_hw11_task1.task1 import SimplifiedEnum


def test_colors_enum():
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")

    a = ColorsEnum()
    assert a.RED == "RED"
    assert a.BLUE == "BLUE"
    assert a.ORANGE == "ORANGE"
    assert a.BLACK == "BLACK"
    with pytest.raises(AttributeError):
        a.GREEN


def test_sizes_enum():
    class SizesEnum(metaclass=SimplifiedEnum):
        __keys = ("XL", "L", "M", "S", "XS")

    assert hasattr(SizesEnum, "XL")
    assert hasattr(SizesEnum, "L")
    assert hasattr(SizesEnum, "M")
    assert hasattr(SizesEnum, "S")
    assert hasattr(SizesEnum, "XS")
    assert not hasattr(SizesEnum, "XXS")


def test_enum_without_using_metaclass():
    class GeomFiguresEnum:
        __keys = ("DOT", "SEGMENT", "TRIANGLE", "SQUARE", "PENTAGON", "HEXAGON")

    assert not hasattr(GeomFiguresEnum, "TRIANGLE")
