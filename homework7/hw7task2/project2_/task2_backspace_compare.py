"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".
    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".
    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".
"""


def handle_with_backspaces(string: str) -> list:
    """One backspace(#) deletes one symbol which is before him in string.

    Return a list of symbols which were not deleted by backspaces.
    """

    backspace = "#"
    backspaces_amount = string.count(backspace)
    symbols = list(string)

    for i in range(backspaces_amount):
        index_backspace = symbols.index(backspace)
        del symbols[index_backspace]
        if index_backspace != 0:
            del symbols[index_backspace - 1]

    return symbols


def backspace_compare(first: str, second: str) -> bool:
    """Take two strings.

    Return True if both strings are equal after some symbols deletion by backspaces.
    """
    return handle_with_backspaces(first) == handle_with_backspaces(second)
