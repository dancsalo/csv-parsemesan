from parsemesan.exceptions import SourceTypeError


def validate(source_type, input_data):
    if source_type == 'arrays' and isinstance(input_data, list):
        return 'arrays'
    elif source_type == 'csv' and isinstance(input_data, bytes):
        return 'csv'
    elif source_type == 'unicode' and isinstance(input_data, str):
        return 'unicode'
    else:
        raise SourceTypeError({})
