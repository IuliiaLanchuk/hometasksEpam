from project1.task1 import (
    count_non_ascii_chars,
    count_punctuation_chars,
    get_longest_diverse_words,
    get_most_common_non_ascii_char,
    get_rarest_char,
)


def test_get_longest_diverse_words():
    actual_result = get_longest_diverse_words("data.txt")
    expected_result = [
        "unmißverständliche",
        "Kollektivschuldiger",
        "Bevölkerungsabschub",
        "Werkstättenlandschaft",
        "Schicksalsfiguren",
        "Selbstverständlich",
        "vernachlässigt",
        "unverständlich",
        "pharmazeutischen",
        "außenpolitisch",
    ]
    assert actual_result == expected_result


def test_get_rarest_char():
    assert get_rarest_char("data.txt") == "X"


def test_count_punctuation_chars():
    assert count_punctuation_chars("data.txt") == 5475


def test_count_non_ascii_chars():
    assert count_non_ascii_chars("data.txt") == 2802


def test_get_most_common_non_ascii_char():
    assert get_most_common_non_ascii_char("data.txt") == "ä"
