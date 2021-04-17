from project_hw11_task1.task1 import SimplifiedEnum


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


def test_attributes_are_accessible():
    a = ColorsEnum()
    assert ColorsEnum.RED == "RED"
    assert a.RED == "RED"
    assert SizesEnum.XL == "XL"
