import os

import pytest
from project2_.task2_table_data_sql import TableData


@pytest.fixture()
def presidents():
    return TableData(
        database_name=os.path.dirname(__file__) + "/example.sqlite",
        table_name="presidents",
    )


def test_data_return_from_database_by_name(presidents):
    assert presidents["Yeltsin"] == ("Yeltsin", 999, "Russia")


def test_no_such_name_in_table(presidents):
    with pytest.raises(KeyError):
        assert presidents["Putin"]


def test_amount_of_lines_in_table(presidents):
    assert len(presidents) == 3


def test_name_in_database_table(presidents):
    assert "Trump" in presidents


def test_name_not_in_database_table(presidents):
    assert "Putin" not in presidents


def test_iterator_protocol_implementation(presidents):
    all_names = [president[0] for president in presidents]

    assert all_names == ["Yeltsin", "Trump", "Big Man Tyrone"]
