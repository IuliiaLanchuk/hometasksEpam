from typing import List, Tuple

import pytest
from project3.task3 import combinations


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [
        (
            ([1, 2], [3, 4]),
            [
                [1, 3],
                [1, 4],
                [2, 3],
                [2, 4],
            ],
        ),
        (
            (["a", "b"], ["c", "d"]),
            [
                ["a", "c"],
                ["a", "d"],
                ["b", "c"],
                ["b", "d"],
            ],
        ),
        ([], [[]]),
    ],
)
def test_combinations(value: Tuple[List], expected_result: List[List]):
    assert combinations(*value) == expected_result
