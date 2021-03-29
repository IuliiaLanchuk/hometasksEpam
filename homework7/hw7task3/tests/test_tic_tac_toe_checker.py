from typing import List

import pytest
from project3_.tic_tac_toe_checker import tic_tac_toe_checker


@pytest.mark.parametrize(
    ("game_board", "expected_result"),
    [
        ([["-", "-", "o"], ["-", "o", "o"], ["x", "x", "x"]], "x wins!"),
        ([["o", "-", "o"], ["-", "o", "o"], ["x", "x", "o"]], "o wins!"),
        ([["-", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]], "unfinished!"),
        ([["x", "o", "x"], ["o", "x", "o"], ["o", "x", "o"]], "draw!"),
    ],
)
def test_tic_tac_toe_checker(game_board: List[List[str]], expected_result: str):
    assert tic_tac_toe_checker(game_board) == expected_result
