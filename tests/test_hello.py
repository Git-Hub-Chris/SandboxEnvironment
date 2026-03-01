"""Test suite for hello module.

This module contains comprehensive tests for all greeting functions.
"""

from hello import farewell, greet, hello


def test_hello() -> None:
    """Test hello function returns correct greeting."""
    assert hello() == "Hello, World!"


def test_greet() -> None:
    """Test greet function with various names."""
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob") == "Hello, Bob!"
    assert greet("Charlie") == "Hello, Charlie!"
    assert greet("") == "Hello, !"


def test_farewell() -> None:
    """Test farewell function with various names."""
    assert farewell("Alice") == "Goodbye, Alice!"
    assert farewell("Bob") == "Goodbye, Bob!"
    assert farewell("Charlie") == "Goodbye, Charlie!"
    assert farewell("") == "Goodbye, !"
