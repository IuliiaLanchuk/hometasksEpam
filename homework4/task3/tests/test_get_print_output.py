import pytest
from project3__get_print_output.task3_get_print_output import my_precious_logger


@pytest.mark.parametrize(
    ("string", "expected_result"),
    [
        ("OK", "OK"),
        ("", ""),
        ("ERROR", "ERROR"),
    ],
)
def test_my_precious_logger_positive(capsys, string, expected_result):
    my_precious_logger(string)
    result = capsys.readouterr()

    assert result.out == expected_result
    assert result.err == ""


def test_my_precious_logger_error(capsys):
    my_precious_logger("error")
    result = capsys.readouterr()

    assert "error" in result.err
    assert result.out == ""
