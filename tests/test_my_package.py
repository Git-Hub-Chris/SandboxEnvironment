import pytest

from my_package.calculator import add, divide
from my_package.hello import hello


def test_my_package_hello() -> None:
    assert hello() == "Hello, World!"


def test_my_package_add() -> None:
    assert add(1, 2) == 3


def test_my_package_divide_by_zero() -> None:
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(1, 0)
