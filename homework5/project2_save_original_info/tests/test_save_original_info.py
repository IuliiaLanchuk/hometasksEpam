import pytest
from task2_oop.save_original_info import custom_sum


def test_custom_sum_func_metadata():
    assert custom_sum.__doc__ == "This function can sum any objects which have __add___"
    assert custom_sum.__name__ == "custom_sum"


@pytest.mark.parametrize(
    ("data", "expected_result"),
    [
        (([1, 2, 3], [4, 5]), [1, 2, 3, 4, 5]),
        ((1, 2, 3, 4), 10),
    ],
)
def test_custom_sum_decorated(capsys, data, expected_result):
    custom_sum(*data)
    without_print = custom_sum.__original_func
    captured = capsys.readouterr()

    assert without_print(*data) == expected_result
    assert str(expected_result) in captured.out
    assert "" in captured.err
