"""Calculator module providing basic arithmetic operations.

This module contains functions for addition, subtraction, multiplication,
and division with proper error handling.
"""


def add(a: float, b: float) -> float:
    """Add two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of a and b.

    Examples:
        >>> add(2, 3)
        5
        >>> add(-1, 1)
        0
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract one number from another.

    Args:
        a: The number to subtract from.
        b: The number to subtract.

    Returns:
        The difference of a and b.

    Examples:
        >>> subtract(5, 3)
        2
        >>> subtract(0, 0)
        0
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The product of a and b.

    Examples:
        >>> multiply(3, 4)
        12
        >>> multiply(-2, 3)
        -6
    """
    return a * b


def divide(a: float, b: float) -> float:
    """Divide one number by another.

    Args:
        a: The dividend.
        b: The divisor.

    Returns:
        The quotient of a divided by b.

    Raises:
        ValueError: If b is zero.

    Examples:
        >>> divide(10, 2)
        5.0
        >>> divide(7, 2)
        3.5
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
