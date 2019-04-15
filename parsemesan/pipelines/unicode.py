from parsemesan.pipelines.helpers import process_unicode


def pipeline(input_data):
    error_dict = dict()
    return process_unicode(input_data, error_dict)
