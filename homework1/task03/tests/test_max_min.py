import pytest
from max_min.task03 import find_maximum_and_minimum


@pytest.mark.parametrize(
    ("file_name", "expected_result"),
    [
        ("homework1/task03/tests/data_1.txt", (-4, 2030)),
        ("homework1/task03/tests/data_2.txt", (5, 5)),
        ("homework1/task03/tests/data_3.txt", (-8, 89)),
        ("homework1/task03/tests/data_4.txt", (9223372036854775807, 0)),
    ],
)
def test_max_min(file_name: str, expected_result: tuple[int, int]):
    actual_result = find_maximum_and_minimum(file_name)

    assert actual_result == expected_result
