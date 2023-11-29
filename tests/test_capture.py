import logging
import pytest

from app.capture import DataCapture


def test_add():
    expected_collection = [3, 5]

    capture = DataCapture()
    capture.add(3)
    capture.add(5)

    assert capture.collection == expected_collection


def test_less():
    expected_numbers = [3, 3]

    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    capture.build_stats()

    result = capture.less(4)

    assert result == expected_numbers


def test_greater():
    expected_numbers = [6, 9]

    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    capture.build_stats()

    result = capture.greater(4)

    assert result == expected_numbers


def test_between():
    expected_numbers = [3, 3, 4, 6]

    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    capture.build_stats()

    result = capture.between(3, 6)

    assert result == expected_numbers


def test_between_fails(caplog):
    expected_message = "Starting number must be less than ending number"

    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)

    with caplog.at_level(logging.INFO):
        capture.build_stats()

    with pytest.raises(ValueError) as ve_info:
        capture.between(6, 3)

    assert "Building stats" in caplog.text
    assert str(ve_info.value) == expected_message
