import pytest


@pytest.fixture()
def _assert_data_fn():
    def assert_data(returned_data, expected_data):
        assert returned_data['headers'] == expected_data['headers']
        assert returned_data['rows'] == expected_data['rows']
    return assert_data


@pytest.fixture()
def _assert_stream_fn():
    def assert_stream(stream, data):
        assert stream.readline().strip().split(',') == data['headers']
    return assert_stream


@pytest.fixture()
def _assert_data_format_fn():
    def assert_data_format(data, valid):
        assert all(k in data for k in ['errors', 'result'])
        assert isinstance(data['errors'], list)
        assert not data['errors'] if valid else data['result'] is None
    return assert_data_format
