from bank import value

def test_hello():
    assert value("Hello, Newman") == 0
    assert value("hello") == 0


def test_h():
    assert value("h") == 20
    assert value("How you doing?") == 20


def test_something_else():
    assert value("What's happening?") == 100
    assert value("There you go, your 100 bucks. Now get the hell out of here, Newman. I don't wanna see your face around this place ever again") == 100
