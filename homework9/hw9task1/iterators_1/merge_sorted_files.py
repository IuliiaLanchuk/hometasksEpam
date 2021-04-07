"""
Write a function that merges integer from sorted files and returns an iterator
file1.txt:
1
3
5
file2.txt:
2
4
6
#>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from pathlib import Path
from typing import Iterator, List, Union


def sorting_data(iter1, iter2) -> int:

    item1 = next(iter1, None)
    item2 = next(iter2, None)
    while item2 or item1:

        if item1 and (not item2 or item1 < item2):
            yield item1
            item1 = next(iter1, None)
        else:
            yield item2
            item2 = next(iter2, None)


def fetching_data(file_path: str) -> int:
    with open(file_path, "r") as file:
        yield from (int(line.rstrip()) for line in file)


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    file_iterator = iter(file_list)
    file_1 = next(file_iterator)
    all_data = fetching_data(file_1)

    while (next_file := next(file_iterator, StopIteration)) != StopIteration:
        all_data = sorting_data(
            (i for i in all_data), (i for i in fetching_data(next_file))
        )

    yield from all_data
