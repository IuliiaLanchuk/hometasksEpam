"""
Homework 7 task3.

Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"
Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"
    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"
"""
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    """Checks if the are some winners.

    If there is "x" winner, function should return "x wins!"
    If there is "o" winner, function should return "o wins!"
    If there is a draw, function should return "draw!"
    If board is unfinished, function should return "unfinished!".
    """

    all_possible_variants = board
    diag_from_left = [item[i] for i, item in enumerate(board)]
    diag_from_right = [item[-i - 1] for i, item in enumerate(board)]
    rows = [list(item) for item in list(zip(*board))]
    all_possible_variants.extend(rows)
    all_possible_variants.extend([diag_from_left, diag_from_right])

    if ["o", "o", "o"] in all_possible_variants:
        return "o wins!"
    if ["x", "x", "x"] in all_possible_variants:
        return "x wins!"
    for item in all_possible_variants:
        if "-" in item:
            return "unfinished!"
    else:
        return "draw!"
