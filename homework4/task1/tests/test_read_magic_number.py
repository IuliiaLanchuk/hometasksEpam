import pytest
from project1_read_file.read_magic_number import read_magic_number


@pytest.fixture(params=["1", "2.99"])
def positive_test_data_file_path(tmp_path, request):
    directory = tmp_path / "dir_for_positive_tests"
    directory.mkdir()
    file_content = request.param
    file_path = directory / "test_data.txt"
    file_path.write_text(file_content)
    return file_path


def test_read_magic_number_positive(positive_test_data_file_path):
    file_path = positive_test_data_file_path
    assert file_path.exists() is True
    assert read_magic_number(str(file_path)) is True


@pytest.fixture(params=["0.99", "3"])
def negative_test_data_file_path(tmp_path, request):
    directory = tmp_path / "dir_for_negative_tests"
    directory.mkdir()
    file_content = request.param
    file_path = directory / "test_data.txt"
    file_path.write_text(file_content)
    return file_path


def test_read_magic_number_negative(negative_test_data_file_path):
    file_path = negative_test_data_file_path
    assert file_path.exists() is True
    assert read_magic_number(str(file_path)) is False


@pytest.fixture(params=[".", " "])
def exception_test_data_file_path(tmp_path, request):
    directory = tmp_path / "dir_for_exception_tests"
    directory.mkdir()
    file_content = request.param
    file_path = directory / "test_data.txt"
    file_path.write_text(file_content)
    return file_path


def test_read_magic_number_exception(exception_test_data_file_path):
    file_path = exception_test_data_file_path
    assert file_path.exists() is True

    with pytest.raises(ValueError, match="In first line a number is required."):
        assert read_magic_number(str(file_path)) is None
