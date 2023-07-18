from seasons import convert
import pytest

def test_invalid_inputs():
    with pytest.raises(SystemExit):
        convert("2010/3/1")
    with pytest.raises(SystemExit):
        convert("cat")
    with pytest.raises(SystemExit):
        convert("2010-13-1")
    with pytest.raises(SystemExit):
        convert("2010-1-32")
    with pytest.raises(SystemExit):
        convert("2010-1-0")
    with pytest.raises(SystemExit):
        convert("2010-0-1")
    with pytest.raises(SystemExit):
        convert("0-1-1")


def test_valid_inputs():
    # When today is 2023-1-17
    assert convert("1889-7-4") == "Seventy million, two hundred thirty-four thousand, five hundred sixty minutes"
    assert convert("1990-11-23") == "Sixteen million, nine hundred nine thousand, nine hundred twenty minutes"
    assert convert("2023-1-1") == "Twenty-three thousand forty minutes"
