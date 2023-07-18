from fuel import convert
from fuel import gauge
import pytest

def test_convert_ints():
    assert convert("3/4") == 75
    assert convert("6/6") == 100
    assert convert("1/999") == 0
    assert convert("99/100") == 99


def test_convert_errors():
    with pytest.raises(ValueError):
        convert("5/4")
    with pytest.raises(ValueError):
        convert("3/cat")
    with pytest.raises(ValueError):
        convert("dog/cat")
    with pytest.raises(ValueError):
        convert("!/;")
    with pytest.raises(ZeroDivisionError):
        convert ("3/0")


def test_gauge():
    assert gauge(75) == '75%'
    assert gauge(32) == '32%'
    assert gauge(100) == 'F'
    assert gauge(99) == 'F'
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'
