import io

from chardet import detect

from parsemesan import config


def peek_stream(stream, length=1):
    pos = stream.tell()
    stream_clip = stream.read(length)
    stream.seek(pos)
    return stream_clip


def convert_stream(string):
    return io.StringIO(string, newline=None)


def detect_encoding(byte_string):
    byte_string_sample = byte_string[:config.CHARDET_BYTES_SAMPLE_SIZE]
    result = detect(byte_string_sample)
    confidence = result.get('confidence', 0)
    encoding = result.get('encoding', '').lower()

    if confidence < config.ENCODING_CONFIDENCE:
        encoding = config.DEFAULT_ENCODING

    return encoding
