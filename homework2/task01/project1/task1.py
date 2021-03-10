"""
Given a file containing text. Complete using only default collections.

1) Find 10 longest words consisting from largest amount of unique symbols
2) Find rarest symbol for document
3) Count every punctuation char
4) Count every non ascii char
5) Find most common non ascii char for document
"""
import string
from typing import List


def file_presettings(file_path: str) -> str:
    """Return unpacked file, encoded in readable format without punctuation."""
    with open(file_path, "r", encoding="unicode_escape") as f:
        text = f.read()
        for p in string.punctuation:
            if p in text:
                text = text.replace(p, "")
        return text


def get_unique_word_symbols(i: str) -> (int):
    """Return amount of unique symbols."""
    return len("".join(set(i)))


def get_longest_diverse_words(file_path: str) -> List[str]:
    """Return 10 longest diverse words."""
    text = file_presettings(file_path)
    all_words = list(dict.fromkeys(text.split()))
    all_words.sort(key=get_unique_word_symbols, reverse=True)
    return all_words[:10]


def get_rarest_char(file_path: str) -> str:
    """Return one single rarest char."""
    with open(file_path, "r", encoding="unicode_escape") as f:
        text = f.read()
        all_chars = {}
        for i in text:
            if i not in all_chars:
                all_chars[i] = 1
            else:
                all_chars[i] += 1
    return min(all_chars.items(), key=lambda item: item[1])[0]


def count_punctuation_chars(file_path: str) -> int:
    """Return the amount of punctuation chars."""
    with open(file_path, "r", encoding="unicode_escape") as f:
        text = f.read()
        counter = 0
        all_punctuation = set(string.punctuation)
        for p in text:
            if p in all_punctuation:
                counter += 1
        return counter


def count_non_ascii_chars(file_path: str) -> int:
    """Return the amount of non ascii chars."""
    text = file_presettings(file_path)
    counter = 0
    for i in text:
        if not i.isascii():
            counter += 1
    return counter


def get_most_common_non_ascii_char(file_path: str) -> str:
    """Return the most common non ascii char."""
    text = file_presettings(file_path)
    non_ascii_chars = {}
    for i in text:
        if not i.isascii():
            if i not in non_ascii_chars:
                non_ascii_chars[i] = 1
            else:
                non_ascii_chars[i] += 1
    return max(non_ascii_chars.items(), key=lambda item: item[1])[0]
