import io
from itertools import repeat
import json


BASE_PATH = 'tests/fixtures/'


def valid_csv_latin_files():
    def _build_payload(name, encoding, line_end):
        return {'encoding': encoding,
                'byte_string': _open_file(f'valid/csv/latin/{name}-{line_end}.csv', True)}

    # Append all UTF files
    name_encodings = zip(['utf-8', 'utf-16-be', 'utf-16-le'], ['ascii', 'utf-16', 'utf-16'])
    files = [_build_payload(name, encoding, line_end)
             for name, encoding in name_encodings
             for line_end in ['cr', 'lf', 'crlf']]

    # Append the rest of the valid latin files
    files.extend([
        {'encoding': 'ascii', 'byte_string': _open_file('valid/csv/latin/ascii.csv', True)},
        {'encoding': 'utf-8-sig', 'byte_string': _open_file('valid/csv/latin/utf-8-sig.csv', True)}
    ])

    return files


def valid_latin_data():
    return {
        'headers': ['header1', 'header2', 'header3'],
        'rows': [
            ['1', 'These', '30-Oct'],
            ['2', 'are', '31-Oct'],
            ['3', 'strings', '1-Nov']
        ]
    }


def valid_csv_non_latin_files():
    def _payload(name, encoding, line_end):
        byte_string = _open_file(f'valid/csv/non-latin/{name}-{line_end}.csv', True)
        return {'encoding': encoding, 'byte_string': byte_string}

    # Append all UTF files
    name_encodings = zip(['utf-8', 'utf-16-be', 'utf-16-le'], ['utf-8', 'utf-16', 'utf-16'])
    return [_payload(name, encoding, line_end)
            for name, encoding in name_encodings
            for line_end in ['cr', 'lf', 'crlf']]


def valid_non_latin_data():
    return {
        'headers': ['AÄBèC', 'AÄBèC1'],
        'rows': [
            ['复制', '复制'],
            ['昨夜のコンサ', 'ートは最高でした'],
            ['1', '2'],
            ['how', 'now'],
            ['ói', 'düb']
        ]
    }


def valid_csv_non_standard_files():
    return [{
        'encoding': 'shift_jis',
        'byte_string': _open_file('valid/csv/non-standard/jis.csv', True)
    }]


def valid_non_standard_data():
    return [{
        'headers': ['昨夜のコンサ', 'ートは最高'],
        'rows': [
            ['でしたの', 'コンサ'],
            ['1', '2']
        ]
    }]


def valid_zero_rows_data():
    return [{
        'headers': ['header1', 'header2'],
        'rows': []
    }]


def valid_data():
    return [valid_latin_data(), valid_non_latin_data()] + valid_non_standard_data() \
           + valid_zero_rows_data()


def valid_csv_files_and_data():
    '''Combine latin and non-latin data and byte strings into one object'''
    files_and_data = []

    # Latin files
    latin_files = valid_csv_latin_files()
    files_and_data.extend([
        {'file': file, 'data': data} for file, data in
        zip(latin_files, repeat(valid_latin_data(), len(latin_files)))
    ])

    # Non-latin files
    non_latin_files = valid_csv_non_latin_files()
    files_and_data.extend([
        {'file': file, 'data': data} for file, data in
        zip(non_latin_files, repeat(valid_non_latin_data(), len(non_latin_files)))
    ])

    # Non-standard files
    non_standard_files = valid_csv_non_standard_files()
    files_and_data.extend([
        {'file': file, 'data': data} for file, data in
        zip(non_standard_files, valid_non_standard_data())
    ])

    return files_and_data


def valid_csv_large_file():
    return {
        'encoding': 'utf-8',
        'byte_string': _open_file('valid/csv/latin/large-table.csv', True)
    }


def valid_csv_streams():
    def _build_stream(file_and_data):
        byte_string = file_and_data['file']['byte_string']
        encoding = file_and_data['file']['encoding']
        return io.StringIO(byte_string.decode(encoding), newline=None)

    return [_build_stream(x) for x in valid_csv_files_and_data()]


def valid_csv_streams_and_data():
    return [{'stream': stream, 'data': file_and_data['data']}
            for stream, file_and_data in zip(valid_csv_streams(), valid_csv_files_and_data())]


def invalid_csv_files():
    '''Combine latin and non-latin data and byte strings into one object'''
    return {
        'source': [{
            'byte_string': _open_file('invalid/encoding/gb18030.csv', True)
        }],
        'data': [{
            'byte_string': _open_file(f'invalid/data/utf-8-sig_{index + 1}.csv', True)
        } for index in range(2)],
        'encoding': [{
            'encoding': 'utf-8',
            'byte_string': _open_file('invalid/encoding/gb18030.csv', True)
        }],
        'filetype': [{
            'byte_string': _open_file(f'invalid/filetype/table.{extension}', True)
        } for extension in ['xml', 'html']]
    }


def invalid_csv_streams():
    def build_stream(extension):
        byte_string = _open_file(f'invalid/filetype/table.{extension}', True)
        return io.StringIO(byte_string.decode(), newline=None)

    return [build_stream(extension) for extension in ['xml', 'html']]


def invalid_data():
    return [
        {  # Blank header
            'headers': ['header1', 'header2', ''],
            'rows': [
                ['1', 'These', '30-Oct'],
                ['2', 'are', '31-Oct'],
                ['3', 'strings', '1-Nov']
            ]
        },
        {  # Non-unique header names
            'headers': ['header1', 'header1', 'header3'],
            'rows': [
                ['1', 'These', '30-Oct'],
                ['2', 'are'],
                ['3', 'strings', '1-Nov']
            ]
        }
    ]


def valid_arrays_objects_and_data():
    def _build_objects(num):
        file = _open_file(f'valid/arrays/table{num + 1}.json')
        return {'object': file['object'], 'data': file['data']}

    return [_build_objects(num) for num in range(2)]


def _open_file(filename, read_as_bytes=False):
    with open(BASE_PATH + filename, 'rb') as file_obj:
        if read_as_bytes:
            return file_obj.read()
        return json.load(file_obj)
