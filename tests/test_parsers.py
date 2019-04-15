import pytest

from parsemesan.helpers import convert_stream
from parsemesan.parsers import parse_csv, parse_arrays
from tests.examples import valid_csv_files_and_data, valid_arrays_objects_and_data


@pytest.mark.parametrize('file_and_data', valid_csv_files_and_data())
def test_csv_and_unicode_parser(file_and_data, _assert_data_fn):
    data = file_and_data['data']
    file = file_and_data['file']
    encoding = file['encoding']
    byte_string = file['byte_string']
    string = byte_string.decode(encoding)

    stream = convert_stream(string)
    output = parse_csv(stream)
    _assert_data_fn(output['data'], data)


@pytest.mark.parametrize('object_and_data', valid_arrays_objects_and_data())
def test_arrays_parser(object_and_data, _assert_data_fn):
    arrays_object = object_and_data['object']
    data = object_and_data['data']

    output = parse_arrays(arrays_object)
    _assert_data_fn(output['data'], data)
