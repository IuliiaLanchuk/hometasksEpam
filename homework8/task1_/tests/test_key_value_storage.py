import os

import pytest
from project_1.task1_key_value_storage import KeyValueStorage

file_path = os.path.dirname(__file__)


def test_values_accessible_as_dict_items_and_as_attributes():
    storage = KeyValueStorage(file_path + "/positive_data.txt")
    assert storage["name"] == "kek"
    assert storage.song == "shadilay"


def test_key_with_builtin_name_raise_error():
    with pytest.raises(
        NameError,
        match="Attribute name conflicts with existing one built-in attribute",
    ):
        KeyValueStorage(file_path + "/nameerror_data.txt")


def test_key_cant_be_assigned_as_an_attribute():
    with pytest.raises(
        ValueError, match="This name cannot be assigned as an attribute name"
    ):
        KeyValueStorage(file_path + "/valueerror_data.txt")


def test_no_such_attribute_raise_error():
    storage = KeyValueStorage(file_path + "/positive_data.txt")
    with pytest.raises(
        AttributeError,
        match="'KeyValueStorage' object has no attribute",
    ):
        assert storage.fake_name
