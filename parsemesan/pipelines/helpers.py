from parsemesan.helpers import convert_stream
from parsemesan.parsers import parse_csv
from parsemesan.validators import validate_filetype, validate_data


def process_unicode(string, error_dict):
    stream = convert_stream(string)
    stream = validate_filetype(stream, error_dict)

    data_and_dialect = parse_csv(stream)
    error_dict['quotechar'] = data_and_dialect['dialect'].quotechar
    error_dict['delimiter'] = data_and_dialect['dialect'].delimiter
    error_dict['doublequote'] = data_and_dialect['dialect'].doublequote
    return validate_data(data_and_dialect['data'], error_dict)
