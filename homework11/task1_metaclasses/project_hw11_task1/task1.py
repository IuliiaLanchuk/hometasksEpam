"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.

from enum import Enum
class ColorsEnum(Enum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"
class SizesEnum(Enum):
    XL = "XL"
    L = "L"
    M = "M"
    S = "S"
    XS = "XS"
Should become:
class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")
class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")
assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"
"""


class SimplifiedEnum(type):
    def __new__(cls, future_class_name, future_class_parents, future_class_attr):
        attrs = [
            value for key, value in future_class_attr.items() if key.endswith("__keys")
        ]
        new_attrs = {item: item for item in attrs[0]}
        return type.__new__(cls, future_class_name, future_class_parents, new_attrs)
