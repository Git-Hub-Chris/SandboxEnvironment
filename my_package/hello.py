"""Greeting module providing various greeting functions.

This module contains functions for generating greetings and farewells.
"""


def hello() -> str:
    """Return a simple hello world greeting.

    Returns:
        A string containing "Hello, World!".

    Examples:
        >>> hello()
        'Hello, World!'
    """
    return "Hello, World!"


def greet(person_name: str) -> str:
    """Generate a personalized greeting.

    Args:
        person_name: The name of the person to greet.

    Returns:
        A personalized greeting string.

    Examples:
        >>> greet("Alice")
        'Hello, Alice!'
        >>> greet("Bob")
        'Hello, Bob!'
    """
    return f"Hello, {person_name}!"


def farewell(person_name: str) -> str:
    """Generate a personalized farewell message.

    Args:
        person_name: The name of the person to bid farewell.

    Returns:
        A personalized farewell string.

    Examples:
        >>> farewell("Alice")
        'Goodbye, Alice!'
        >>> farewell("Bob")
        'Goodbye, Bob!'
    """
    return f"Goodbye, {person_name}!"
