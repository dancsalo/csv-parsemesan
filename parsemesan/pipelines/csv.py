from parsemesan.helpers import detect_encoding
from parsemesan.pipelines.helpers import process_unicode
from parsemesan.validators import validate_encoding


def pipeline(input_data):
    error_dict = dict()

    encoding = detect_encoding(input_data)
    error_dict['encoding'] = encoding
    byte_string, encoding = validate_encoding(input_data, encoding, error_dict)

    string = byte_string.decode(encoding)
    return process_unicode(string, error_dict)
