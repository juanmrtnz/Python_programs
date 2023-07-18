from plates import is_valid

def test_starts_with_two_letters():
    assert is_valid("505050") == False
    assert is_valid("C5") == False
    assert is_valid("CS50") == True


def test_minlenghtis2_maxlengthis6():
    assert is_valid("C") == False
    assert is_valid("CS") == True
    assert is_valid("ABCD50") == True
    assert is_valid("ABCDE50") == False


def test_numbers_at_end():
    assert is_valid("CS50P") == False
    assert is_valid("CS1ABC") == False
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False


def test_firstnumber_not_zero():
    assert is_valid("CS05") == False
    assert is_valid("ABC012") == False


def test_no_punctuation():
    assert is_valid("CS 50") == False
    assert is_valid("CS,50") == False
    assert is_valid("CS.50") == False
    assert is_valid("CS:50") == False
    assert is_valid("CS;50") == False
