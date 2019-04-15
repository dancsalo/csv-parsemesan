from parsemesan.exceptions import EncodingError


def validate(byte_string, encoding, error_dict):
    try:
        byte_string.decode(encoding)
    except UnicodeDecodeError:
        raise EncodingError(error_dict)

    return byte_string, encoding
