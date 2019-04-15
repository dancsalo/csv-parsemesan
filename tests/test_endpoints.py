import pytest

from parsemesan.locales import VALIDATION_ERRORS, get_message
from parsemesan.parsemesan import get_valid_formats, parse_data
from tests.examples import (valid_arrays_objects_and_data, valid_csv_files_and_data,
                            invalid_csv_files, valid_csv_large_file)


@pytest.mark.parametrize('object_and_data', valid_arrays_objects_and_data())
def test_parse_data_valid_arrays(object_and_data, _assert_data_format_fn, _assert_data_fn):
    obj = object_and_data['object']
    valid_data = object_and_data['data']

    returned = parse_data(source_type='arrays', input_data=obj)
    _assert_data_format_fn(returned, valid=True)
    _assert_data_fn(returned['result'], valid_data)


@pytest.mark.parametrize('file_and_data', valid_csv_files_and_data())
def test_parse_data_valid_csv(file_and_data, _assert_data_format_fn, _assert_data_fn):
    file = file_and_data['file']
    valid_data = file_and_data['data']
    byte_string = file['byte_string']

    returned = parse_data(source_type='csv', input_data=byte_string)
    _assert_data_format_fn(returned, valid=True)
    _assert_data_fn(returned['result'], valid_data)


@pytest.mark.parametrize('file_and_data', valid_csv_files_and_data())
def test_parse_data_valid_unicode(file_and_data, _assert_data_format_fn, _assert_data_fn):
    file = file_and_data['file']
    valid_data = file_and_data['data']
    utf8_string = file['byte_string'].decode(file['encoding'])

    returned = parse_data(source_type='unicode', input_data=utf8_string)
    _assert_data_format_fn(returned, valid=True)
    _assert_data_fn(returned['result'], valid_data)


@pytest.mark.parametrize('error_type', ['source', 'encoding', 'filetype', 'data'])
def test_parse_data_invalid(error_type, _assert_data_format_fn):
    for file in invalid_csv_files()[error_type]:
        source_type = 'arrays' if error_type == 'source' else 'csv'

        returned = parse_data(source_type, file['byte_string'])

        _assert_data_format_fn(returned, valid=False)
        if error_type == 'data':
            error = returned['errors'][0]
            if error['type'] == 'blank_header':
                expected = get_message(VALIDATION_ERRORS[error['type']], indexes=error['indexes'])
            else:
                expected = get_message(VALIDATION_ERRORS[error['type']],
                                       headers=error['headers'], indexes=error['indexes'])
            assert error['detail'] == expected
        else:
            found = [x['detail'] for x in returned['errors'] if error_type in x['detail']]
            assert len(found) == 1


def test_parse_data_large_csv(_assert_data_format_fn):
    '''Ensure this test passes quickly.'''
    input_data = valid_csv_large_file()['byte_string']

    returned = parse_data('csv', input_data)
    _assert_data_format_fn(returned, valid=True)


def test_get_valid_formats(_assert_data_format_fn):
    assert get_valid_formats() == {'formats': ['arrays', 'csv', 'unicode']}
