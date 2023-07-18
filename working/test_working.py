from working import convert
import pytest

def test_invalid_inputs():
    with pytest.raises(ValueError):
        convert("9AM to 5PM")
    with pytest.raises(ValueError):
        convert("9:00 to 17:00")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("10:7 AM - 5:1 PM")
    with pytest.raises(ValueError):
        convert("9am to 5pm")

def test_invalid_hours():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("5 AM to 13 PM")

def test_invalid_minutes():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("9 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9:7 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("9 AM to 5:4 PM")


def test_valid_inputs():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("7:30 AM to 3:55 PM") == "07:30 to 15:55"
    assert convert("2:10 PM to 8:45 PM") == "14:10 to 20:45"
    assert convert("9 AM to 5 AM") == "09:00 to 05:00"
