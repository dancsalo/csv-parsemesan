from parsemesan.locales import VALIDATION_ERRORS, get_message
from parsemesan.exceptions import DataError


def validate(data, error_dict):
    _validate_header_blanks(data['headers'], error_dict)
    _validate_header_duplicates(data['headers'], error_dict)
    return {'headers': data['headers'], 'rows': data['rows']}


def _validate_header_blanks(headers, error_dict):
    '''Check headers for blanks.'''
    indexes_with_errors = [idx for idx, header in enumerate(headers, 1) if not header]
    if indexes_with_errors:
        _raise_data_error(error_dict, 'blank_header', indexes_with_errors)


def _validate_header_duplicates(headers, error_dict):
    '''Check headers for duplicates.'''
    duplicates = [(idx, header) for idx, header in enumerate(headers, 1)
                  if headers.count(header) > 1]
    if duplicates:
        _raise_data_error(error_dict, 'duplicate_header', [i[0] for i in duplicates],
                          [i[1] for i in duplicates])


def _raise_data_error(error_dict, error_type, indexes, headers=None):
    error_dict['type'] = error_type
    error_dict['indexes'] = indexes
    if not headers:
        error_dict['detail'] = get_message(VALIDATION_ERRORS[error_type], indexes=indexes)
    else:
        error_dict['headers'] = headers
        error_dict['detail'] = get_message(VALIDATION_ERRORS[error_type],
                                           headers=headers, indexes=indexes)
    raise DataError(error_dict)
