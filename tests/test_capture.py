import logging
import pytest

from app.capture import DataCapture


@pytest.fixture
def data_capture_mock():
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    return capture


def test_add():
    expected_collection = [3, 5]

    capture = DataCapture()
    capture.add(3)
    capture.add(5)

    assert capture.collection == expected_collection


def test_less(data_capture_mock):
    expected_numbers = [3, 3]

    data_capture_mock.build_stats()

    result = data_capture_mock.less(4)

    assert result == expected_numbers


def test_greater(data_capture_mock):
    expected_numbers = [6, 9]

    data_capture_mock.build_stats()

    result = data_capture_mock.greater(4)

    assert result == expected_numbers


def test_between(data_capture_mock):
    expected_numbers = [3, 3, 4, 6]

    data_capture_mock.build_stats()

    result = data_capture_mock.between(3, 6)

    assert result == expected_numbers


def test_between_fails(data_capture_mock, caplog):
    expected_message = "Starting number must be less than ending number"

    with caplog.at_level(logging.INFO):
        data_capture_mock.build_stats()

    with pytest.raises(ValueError) as ve_info:
        data_capture_mock.between(6, 3)

    assert "Building stats" in caplog.text
    assert str(ve_info.value) == expected_message
