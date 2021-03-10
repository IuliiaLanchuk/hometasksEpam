from project1.task1 import (
    count_non_ascii_chars,
    count_punctuation_chars,
    get_longest_diverse_words,
    get_most_common_non_ascii_char,
    get_rarest_char,
)

FILE_PATH = "data.txt"


def test_get_longest_diverse_words():
    actual_result = get_longest_diverse_words(FILE_PATH)
    expected_result = [
        "unmißverständliche",
        "Bevölkerungsabschub",
        "Kollektivschuldiger",
        "Werkstättenlandschaft",
        "Schicksalsfiguren",
        "Selbstverständlich",
        "Fingerabdrucks",
        "Friedensabstimmung",
        "außenpolitisch",
        "Seinsverdichtungen",
    ]
    assert actual_result == expected_result


def test_get_rarest_char():
    assert get_rarest_char(FILE_PATH) == "›"


def test_count_punctuation_chars():
    assert count_punctuation_chars(FILE_PATH) == 5305


def test_count_non_ascii_chars():
    assert count_non_ascii_chars(FILE_PATH) == 2972


def test_get_most_common_non_ascii_char():
    assert get_most_common_non_ascii_char(FILE_PATH) == "ä"
