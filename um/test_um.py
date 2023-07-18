from um import count

def test_words_with_um():
    assert count("yummy") == 0
    assert count("JUMPING") == 0
    assert count("Umami") == 0
    assert count("scrum.") == 0


def test_only_um():
    assert count("um") == 1
    assert count("Um,") == 1
    assert count("UM...") == 1
    assert count("... um?") == 1


def test_um_in_phrases():
    assert count("Um, yes.") == 1
    assert count("Um... I don't know") == 1
    assert count("No, but... um?") == 1
    assert count("Um... very yummy, indeed") == 1
    assert count("I'm Scrum, James Scrum.") == 0
    assert count("How many more, um, tests, um, do I need to do?") == 2
    assert count("Um? Well, um... just this one, um, I think") == 3


