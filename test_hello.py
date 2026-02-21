from hello import hello, greet, farewell, add


def test_hello():
    assert hello() == "Hello, World!"


def test_greet():
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob") == "Hello, Bob!"


def test_farewell():
    assert farewell("Alice") == "Goodbye, Alice!"
    assert farewell("Bob") == "Goodbye, Bob!"


def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
