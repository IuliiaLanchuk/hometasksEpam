import os

from iterators_1.merge_sorted_files import merge_sorted_files

path = os.path.dirname(__file__)


def test_merge_three_sorted_files():
    assert list(
        merge_sorted_files(
            [path + "/file1.txt", path + "/file2.txt", path + "/file3.txt"]
        )
    ) == [-7, 1, 2, 3, 4, 9]


def test_merge_two_files_with_repeated_numbers():
    assert list(merge_sorted_files([path + "/file4.txt", path + "/file5.txt"])) == [
        -1,
        1,
        2,
        2,
        2,
        3,
        3,
        3,
    ]


def test_merge_two_empty_files():
    assert list(merge_sorted_files([path + "/file6.txt", path + "/file7.txt"])) == []
