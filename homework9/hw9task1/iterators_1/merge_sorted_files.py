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
from heapq import merge
from pathlib import Path
from typing import Iterator, List, Union


def fetching_data(file_path: str):
    with open(file_path, "r") as file:
        yield from (int(line.rstrip()) for line in file)


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    all_data = (fetching_data(file) for file in file_list)
    return iter(merge(*all_data))
