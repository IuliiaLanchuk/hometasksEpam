import pytest
from project5_optional.task5_optional import fizzbuzz


@pytest.mark.parametrize(
    ("number", "expected_result"),
    [
        (1, ["1"]),
        (
            15,
            [
                "1",
                "2",
                "fizz",
                "4",
                "buzz",
                "fizz",
                "7",
                "8",
                "fizz",
                "buzz",
                "11",
                "fizz",
                "13",
                "14",
                "fizz buzz",
            ],
        ),
    ],
)
def test_fizzbuzz_positive(number, expected_result):
    assert list(fizzbuzz(number)) == expected_result


def test_fizzbuzz_exception():
    with pytest.raises(ValueError, match="Input error. Required positive number"):
        list(fizzbuzz(-1))
