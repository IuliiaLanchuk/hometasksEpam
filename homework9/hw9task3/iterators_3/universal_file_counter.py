"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
For dir with two files from hw1.py:
#>>> universal_file_counter(test_dir, "txt")
6
#>>> universal_file_counter(test_dir, "txt", str.split)
6
"""
import os
from os.path import getsize
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    amount_of_tokens_or_lines = 0
    all_files = [file for file in os.listdir(dir_path) if file.endswith(file_extension)]
    for file_name in all_files:
        file_path = f"{dir_path}/{file_name}"
        if getsize(file_path) != 0:
            with open(file_path, "r") as file:
                amount_of_tokens_or_lines += (
                    sum(len(token) for token in map(tokenizer, file))
                    if tokenizer
                    else sum(1 for line in file)
                )

    return amount_of_tokens_or_lines
