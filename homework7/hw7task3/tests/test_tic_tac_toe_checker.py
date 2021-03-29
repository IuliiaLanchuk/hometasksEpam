from project3_.tic_tac_toe_checker import tic_tac_toe_checker


def test_tic_tac_toe_checker_return_x_wins_horizontally():
    assert (
        tic_tac_toe_checker([["-", "-", "o"], ["-", "o", "o"], ["x", "x", "x"]])
        == "x wins!"
    )


def test_tic_tac_toe_checker_return_o_wins_diagonally():
    assert (
        tic_tac_toe_checker([["o", "-", "o"], ["-", "o", "o"], ["o", "x", "-"]])
        == "o wins!"
    )


def test_tic_tac_toe_checker_return_x_wins_vertically():
    assert (
        tic_tac_toe_checker([["o", "x", "o"], ["-", "x", "o"], ["o", "x", "-"]])
        == "x wins!"
    )


def test_tic_tac_toe_checker_with_unfilled_board():
    assert (
        tic_tac_toe_checker([["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]])
        == "unfinished!"
    )


def test_tic_tac_toe_checker_return_unfinished():
    assert (
        tic_tac_toe_checker([["-", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]])
        == "unfinished!"
    )


def test_tic_tac_toe_checker_no_winner_return_draw():
    assert (
        tic_tac_toe_checker([["x", "o", "x"], ["o", "x", "o"], ["o", "x", "o"]])
        == "draw!"
    )
