from parsemesan.locales.errors import VALIDATION as VALIDATION_ERRORS


def get_message(path, **kwargs):
    return path.format(**kwargs)
