import pytest

from parsemesan.helpers import peek_stream, convert_stream, detect_encoding
from tests.examples import valid_csv_files_and_data, valid_csv_streams_and_data


@pytest.mark.parametrize('stream_and_data', valid_csv_streams_and_data())
def test_peek_stream(stream_and_data, _assert_stream_fn):
    stream = stream_and_data['stream']
    data = stream_and_data['data']

    _ = peek_stream(stream)
    _assert_stream_fn(stream, data)


@pytest.mark.parametrize('file_and_data', valid_csv_files_and_data())
def test_convert_stream(file_and_data, _assert_stream_fn):
    data = file_and_data['data']
    encoding = file_and_data['file']['encoding']
    byte_string = file_and_data['file']['byte_string']
    string = byte_string.decode(encoding)

    stream = convert_stream(string)
    _assert_stream_fn(stream, data)


@pytest.mark.parametrize('file_and_data', valid_csv_files_and_data())
def test_detect_encoding(file_and_data):
    encoding = file_and_data['file']['encoding']
    byte_string = file_and_data['file']['byte_string']

    assert encoding == detect_encoding(byte_string)
