import pytest

from parsemesan import exceptions
from parsemesan.validators import (validate_source, validate_encoding, validate_filetype,
                                   validate_data)
from tests.examples import (valid_csv_files_and_data, invalid_csv_files, valid_csv_streams,
                            invalid_csv_streams, valid_data, invalid_data)


def test_source():
    file_and_data = valid_csv_files_and_data()[0]
    byte_string = file_and_data['file']['byte_string']

    with pytest.raises(exceptions.SourceTypeError):
        validate_source(source_type='invalid_source_type', input_data=byte_string)
    with pytest.raises(exceptions.SourceTypeError):
        validate_source(source_type='csv', input_data=['invalid', 'csv', 'input', 'data'])


@pytest.mark.parametrize('file_and_data', valid_csv_files_and_data())
def test_encoding_valid(file_and_data):
    file = file_and_data['file']
    byte_string = file['byte_string']
    encoding = file['encoding']

    validate_encoding(byte_string, encoding, {})


@pytest.mark.parametrize('file', invalid_csv_files()['encoding'])
def test_encoding_invalid(file):
    byte_string = file['byte_string']
    encoding = file['encoding']

    with pytest.raises(exceptions.EncodingError):
        validate_encoding(byte_string, encoding, {})


@pytest.mark.parametrize('stream', valid_csv_streams())
def test_filetype_valid(stream):
    validate_filetype(stream, {})


@pytest.mark.parametrize('stream', invalid_csv_streams())
def test_filetype_invalid(stream):
    with pytest.raises(exceptions.FileTypeError):
        validate_filetype(stream, {})


@pytest.mark.parametrize('data', valid_data())
def test_data(data, _assert_data_fn):
    returned_data = validate_data(data, {})
    assert isinstance(returned_data['rows'], list)
    for value in returned_data['rows']:
        assert isinstance(value, list)
    _assert_data_fn(returned_data, data)


@pytest.mark.parametrize('data', invalid_data())
def test_data_raises(data):
    with pytest.raises(exceptions.DataError):
        validate_data(data, {})
