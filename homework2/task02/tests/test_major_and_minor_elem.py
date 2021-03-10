import pytest
from project2.task2 import major_and_minor_elem


@pytest.mark.parametrize(
    ("a", "expected_result"),
    [
        ([2, 2, 1, 3, 1, 2], (2, 3)),
        ([1, 1], (1, 1)),
        ([0], (0, 0)),
    ],
)
def test_major_and_minor_elem(a: list[int], expected_result: (int, int)):
    assert major_and_minor_elem(a) == expected_result
