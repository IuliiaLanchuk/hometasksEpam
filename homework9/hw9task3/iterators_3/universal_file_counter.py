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
    for file_name in os.listdir(dir_path):
        if file_name.endswith(file_extension) and getsize(file_name) != 0:
            with open(file_name, "r") as file:
                if not tokenizer:
                    amount_of_tokens_or_lines += sum(1 for line in file)
                else:
                    all_data = file.read()
                    amount_of_tokens_or_lines += sum(1 for item in tokenizer(all_data))

    return amount_of_tokens_or_lines
