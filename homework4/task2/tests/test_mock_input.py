from unittest.mock import Mock, patch

import pytest
from project2_mock_input.task2_mock_input import count_dots_on_i


@patch("requests.get")
def test_count_dots_on_i_with_mock_positive(mock):
    mock.return_value = Mock(text="iiaiaaaaIIII")
    result = count_dots_on_i("some_url")
    mock.assert_called_with("some_url")
    assert result == 3


@patch("requests.get", side_effect=Exception("Unknown url"))
def test_count_dots_on_i_exception(mock):
    with pytest.raises(ValueError, match="Unreachable"):
        count_dots_on_i("https://example.com/")

    mock.assert_called_with("https://example.com/")
