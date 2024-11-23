from unittest.mock import patch
from fetch_www import parse, fetch_net


@patch('fetch_www.fetch_net')
def test_parse_from_fetch_net(mock_get):
    mock_get.return_value = "def"
    assert parse() == "def123"

@patch('fetch_www.fetch_net')
@patch('fetch_www.parse')
def test_parse_from_fetch_net(mock_parse, mock_get):
    mock_get.return_value = "def"
    mock_parse.return_value = "abc"
    assert fetch_net() == mock_parse.return_value