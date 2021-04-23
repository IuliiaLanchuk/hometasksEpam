from project_hw11_task1.task1 import SimplifiedEnum


def test_color_attributes_are_accessible_using_metaclass():
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")

    a = ColorsEnum()
    assert ColorsEnum.RED == "RED"
    assert a.RED == "RED"


def test_size_attributes_are_accessible_using_metaclass():
    class SizesEnum(metaclass=SimplifiedEnum):
        __keys = ("XL", "L", "M", "S", "XS")

    assert SizesEnum.M == "M"
    assert hasattr(SizesEnum, "XL")


def test_attributes_are_inaccessible_without_using_metaclass():
    class GeomFiguresEnum:
        __keys = ("DOT", "SEGMENT", "TRIANGLE", "SQUARE", "PENTAGON", "HEXAGON")

    assert not hasattr(GeomFiguresEnum, "TRIANGLE")
