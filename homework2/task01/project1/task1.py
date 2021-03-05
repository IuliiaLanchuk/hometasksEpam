"""
Given a file containing text. Complete using only default collections.

1) Find 10 longest words consisting from largest amount of unique symbols
2) Find rarest symbol for document
3) Count every punctuation char
4) Count every non ascii char
5) Find most common non ascii char for document
"""
import re
from collections import Counter
from typing import List


def file_presettings(file_path: str) -> str:
    r"""
    Return unpacked file, encode in readable format.

    First sub() deletes '\n' between lines. Second sub() remove punctuation.
    """
    with open(file_path, "r") as f:
        text = f.read()
        a = text.encode().decode("unicode_escape")
        filtered_text = re.sub(r"[\n]", " ", a)
        return re.sub(r"[^\w]", " ", filtered_text)


def get_longest_diverse_words(file_path: str) -> List[str]:
    """Return 10 longest diverse words."""
    text = file_presettings(file_path)
    all_words = set(text.split())
    result = []
    result.extend(all_words)
    result.sort(key=lambda i: (len("".join(set(i))), i[0]), reverse=True)
    return result[:10]


def get_rarest_char(file_path: str) -> str:
    """Return one single rarest char."""
    text = file_presettings(file_path)
    all_data = Counter(text)
    return all_data.most_common()[:-2:-1][0][0]


def count_punctuation_chars(file_path: str) -> int:
    """Return the amount of punctuation chars."""
    with open(file_path, "r") as f:
        text = f.read()
        a = text.encode().decode("unicode_escape")
        filtered_text = re.sub(r"[\n]", "", a)
        kill_punctuation = re.sub(r"[\w]", "", filtered_text)
        kill_spaces = re.sub(r" ", "", kill_punctuation)
        result = Counter(kill_spaces)
        return sum(result.values())


def count_non_ascii_chars(file_path: str) -> int:
    """Return the amount of non ascii chars."""
    text = file_presettings(file_path)
    counter = 0
    for i in text:
        if 0 <= ord(i) <= 127:
            continue
        else:
            counter += 1
    return counter


def get_most_common_non_ascii_char(file_path: str) -> str:
    """Return the most common non ascii char."""
    text = file_presettings(file_path)
    non_ascii_chars = []
    for i in text:
        if 0 <= ord(i) <= 127:
            continue
        else:
            non_ascii_chars.append(i)
    return Counter(non_ascii_chars).most_common(1)[0][0]
