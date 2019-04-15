class ValidateError(Exception):
    def __init__(self, error_dict):
        if 'detail' not in error_dict:
            error_dict['detail'] = getattr(self, 'detail', None)
        self.payload = error_dict

    def get_payload(self):
        return self.payload


class SourceTypeError(ValidateError):
    detail = 'source'


class EncodingError(ValidateError):
    detail = 'encoding'


class FileTypeError(ValidateError):
    detail = 'filetype'


class DataError(ValidateError):
    detail = 'data'
