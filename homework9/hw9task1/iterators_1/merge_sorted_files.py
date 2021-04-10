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


def sorting_data(*iters: Iterator):
    temp_list = []
    merge_list = iters[0]
    for i in range(1, len(iters)):
        iter2 = iters[i]
        item1 = next(merge_list, None)
        item2 = next(iter2, None)
        while item2 or item1:
            if item1 and (not item2 or item1 < item2):
                temp_list.append(item1)
                item1 = next(merge_list, None)
            else:
                temp_list.append(item2)
                item2 = next(iter2, None)
        merge_list = iter(temp_list[:])
        temp_list.clear()
    return merge_list


def fetching_data(file_path: str) -> Iterator:
    with open(file_path, "r") as file:
        yield from (int(line.rstrip()) for line in file)


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    all_data = (fetching_data(file) for file in file_list)
    return sorting_data(*all_data)
