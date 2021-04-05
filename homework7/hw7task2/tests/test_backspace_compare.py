from project2_.task2_backspace_compare import backspace_compare


def test_backspaces_in_a_row():
    assert backspace_compare("abc###R", "R")


def test_backspaces_in_different_places():
    assert backspace_compare("##aaa#b#bn##", "aa")


def test_backspaces_in_string_beginning():
    assert backspace_compare("###cb", "cb")


def test_backspaces_in_string_end():
    assert backspace_compare("aaa#######", "")


def test_both_strings_contains_only_backspaces():
    assert backspace_compare("###", "######")


def test_strings_are_different():
    assert not backspace_compare("a#c", "b")


def test_one_string_is_a_backspace_another_string_is_empty():
    assert backspace_compare("#", "")
