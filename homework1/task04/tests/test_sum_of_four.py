import pytest
from sum_of_four.task04 import check_sum_of_four


@pytest.mark.parametrize(
    ("a", "b", "c", "d", "expected_result"),
    [
        ([-2, -3], [-3, 8], [3, 8], [2, 2], 2),
        ([], [], [], [], 0),
        ([0], [0], [0], [0], 1),
    ],
)
def test_sum_of_four(
    a: list[int], b: list[int], c: list[int], d: list[int], expected_result: int
):
    assert check_sum_of_four(a, b, c, d) == expected_result
