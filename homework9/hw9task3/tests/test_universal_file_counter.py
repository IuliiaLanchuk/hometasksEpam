from pathlib import Path

from iterators_3.universal_file_counter import universal_file_counter


def test_universal_file_counter_with_tokenizer_data_split_by_space():
    assert universal_file_counter(Path().absolute(), "txt", str.split) == 11
    assert (
        universal_file_counter(Path().absolute(), "txt", lambda data: data.split())
        == 11
    )


def test_universal_file_counter_without_tokenizer():
    assert universal_file_counter(Path().absolute(), "txt") == 8


def test_universal_file_counter_with_tokenizer_data_split_by_symbol():
    assert (
        universal_file_counter(Path().absolute(), "txt", lambda data: data.split("c"))
        == 5
    )
