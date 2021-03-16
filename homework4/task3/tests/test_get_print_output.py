from project3__get_print_output.task3_get_print_output import my_precious_logger


def test_my_precious_logger_positive(capsys):
    my_precious_logger("OK")
    result = capsys.readouterr()

    assert result.out == "OK"


def test_my_precious_logger_error(capsys):
    my_precious_logger("error")
    result = capsys.readouterr()

    assert "error" in result.err
