from numb3rs import validate

def test_correct_IPaddress_format():
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("196.18.112.1") == True
    assert validate("512.0.0.0") == False
    assert validate("0.0.0.512") == False
    

def test_incorrect_IPaddress_format():
    assert validate("255.255.255.-1") == False
    assert validate("100-100-100-100") == False
    assert validate("cat.dog.cs50.P") == False
    assert validate("cat") == False