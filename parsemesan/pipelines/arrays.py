from parsemesan.parsers import parse_arrays
from parsemesan.validators import validate_data


def pipeline(input_data):
    data = parse_arrays(input_data)
    return validate_data(data['data'], error_dict={})
