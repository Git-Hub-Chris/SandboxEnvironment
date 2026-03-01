"""Test suite for calculator module.

This module contains comprehensive tests for all calculator functions
including edge cases and error conditions.
"""

import pytest

from sandboxenvironment.calculator import add, divide, multiply, subtract


def test_add() -> None:
    """Test addition function with various inputs."""
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(1.5, 2.5) == 4.0
    assert add(-5, -3) == -8


def test_subtract() -> None:
    """Test subtraction function with various inputs."""
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0
    assert subtract(10.5, 5.5) == 5.0
    assert subtract(-3, 2) == -5


def test_multiply() -> None:
    """Test multiplication function with various inputs."""
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6
    assert multiply(0, 100) == 0
    assert multiply(2.5, 4) == 10.0
    assert multiply(-5, -5) == 25


def test_divide() -> None:
    """Test division function with various inputs."""
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5
    assert divide(-6, 3) == -2.0
    assert divide(1, 3) == pytest.approx(0.333333, rel=1e-5)
    assert divide(100, 0.5) == 200.0


def test_divide_by_zero() -> None:
    """Test that division by zero raises ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(1, 0)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(0, 0)
