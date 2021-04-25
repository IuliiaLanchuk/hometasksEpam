import pytest
from project_hw11_task1.task1 import SimplifiedEnum


def test_attributes_of_enum_are_accessible_via_instance_and_class():
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("RED", "BLUE", "ORANGE")

    assert ColorsEnum.RED == "RED"

    a = ColorsEnum()
    assert a.BLUE == "BLUE"
    assert a.ORANGE == "ORANGE"
    with pytest.raises(AttributeError):
        a.GREEN


def test_attributes_of_enum_are_inaccessible_without_use_metaclass():
    class GeomFiguresEnum:
        __keys = ("DOT", "SEGMENT", "TRIANGLE")

    with pytest.raises(AttributeError):
        GeomFiguresEnum.TRIANGLE
