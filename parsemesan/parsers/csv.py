import csv

from parsemesan.config import SNIFF_BYTES_SAMPLE_SIZE
from parsemesan.helpers import peek_stream


def _get_dialect(stream):
    try:
        stream_clip = peek_stream(stream, SNIFF_BYTES_SAMPLE_SIZE)
        dialect = csv.Sniffer().sniff(stream_clip, delimiters=',')
        if not dialect.escapechar:
            dialect.doublequote = True
    except csv.Error:
        dialect = csv.excel

    return dialect


def parse(stream):
    dialect = _get_dialect(stream)
    reader = csv.reader(stream, dialect)
    headers = next(reader)
    rows = list(reader)
    return {'data': {'headers': headers, 'rows': rows}, 'dialect': dialect}
