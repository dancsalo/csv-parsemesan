from parsemesan.exceptions import SourceTypeError, EncodingError, FileTypeError, DataError
from parsemesan.pipelines import pipeline_arrays, pipeline_csv, pipeline_unicode
from parsemesan.validators import validate_source


PIPELINES = {
    'arrays': pipeline_arrays,
    'csv': pipeline_csv,
    'unicode': pipeline_unicode
}


def get_valid_formats():
    return {'formats': list(PIPELINES.keys())}


def parse_data(source_type, input_data):
    try:
        matched_type = validate_source(source_type, input_data)
        data = PIPELINES[matched_type](input_data)
        return {'errors': [], 'result': data}
    except (EncodingError, SourceTypeError, FileTypeError, DataError) as err:
        return {'errors': [err.get_payload()], 'result': None}
