import pytest
from project_1.task1_key_value_storage import KeyValueStorage


def test_values_accessible_as_dict_items_and_as_attributes():
    storage = KeyValueStorage("homework8/task1_/tests/positive_data.txt")
    assert storage["name"] == "kek"
    assert storage.song == "shadilay"


def test_key_with_builtin_name_raise_error():
    with pytest.raises(
        NameError,
        match="Attribute name conflicts with existing one built-in attribute",
    ):
        KeyValueStorage("homework8/task1_/tests/nameerror_data.txt")


def test_key_cant_be_assigned_as_an_attribute():
    with pytest.raises(
        ValueError, match="This name cannot be assigned as an attribute name"
    ):
        KeyValueStorage("homework8/task1_/tests/valueerror_data.txt")
