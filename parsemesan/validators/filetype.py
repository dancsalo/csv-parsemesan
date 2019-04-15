from parsemesan.exceptions import FileTypeError
from parsemesan.helpers import peek_stream


def validate(stream, error_dict):
    _check_xml(stream, error_dict)
    _check_html(stream, error_dict)
    return stream


def _check_html(stream, error_dict):
    '''Check for DOCTYPE or HTML tags.'''
    if peek_stream(stream, 5) == ('<!DOC' or '<html'):
        error_dict['type'] = 'html'
        raise FileTypeError(error_dict)


def _check_xml(stream, error_dict):
    '''Check for the XML start characters.'''
    if peek_stream(stream, 2) == '<?':
        error_dict['type'] = 'xml'
        raise FileTypeError(error_dict)
