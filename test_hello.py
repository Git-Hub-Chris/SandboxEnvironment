from hello import hello, greet, farewell


def test_hello():
    assert hello() == "Hello, World!"


def test_greet():
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob") == "Hello, Bob!"


def test_farewell():
    assert farewell("Alice") == "Goodbye, Alice!"
    assert farewell("Bob") == "Goodbye, Bob!"
