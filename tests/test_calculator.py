import pytest
from src.calculator import SimpleMath


# Fixture to create a SimpleMath instance to prevent code duplication
@pytest.fixture
def math_app():
    return SimpleMath()


def test_add(math_app):
    assert math_app.add(2, 3) == 5
    assert math_app.add(-1, 1) == 0
    assert math_app.add(-5, -5) == -10


def test_subtract(math_app):
    assert math_app.subtract(10, 5) == 5
    assert math_app.subtract(-5, 5) == -10
    assert math_app.subtract(2.5, 1.5) == 1.0


def test_multiply(math_app):
    assert math_app.multiply(3, 4) == 12
    assert math_app.multiply(-3, 3) == -9
    assert math_app.multiply(2.5, 2) == 5.0


def test_divide(math_app):
    assert math_app.divide(10, 2) == 5.0
    assert math_app.divide(-10, -2) == 5.0
    assert math_app.divide(7.5, 2.5) == 3.0


def test_divide_by_zero(math_app):
    """Testing division by zero raises ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        math_app.divide(10, 0)


def test_divide_decimal_precision(math_app):
    """Testing decimal precision in division."""
    assert math_app.divide(1, 3) == pytest.approx(0.3333333333)


def test_add_decimals(math_app):
    """Testing decimal precision in addition."""
    assert math_app.add(0.1, 0.2) == pytest.approx(0.3)


def test_invalid_input(math_app):
    """Testing that invalid inputs raise TypeError."""
    with pytest.raises(TypeError, match="Input values must be numbers."):
        math_app.add("a", 2)
    with pytest.raises(TypeError, match="Input values must be numbers."):
        math_app.subtract(1, None)
    with pytest.raises(TypeError, match="Input values must be numbers."):
        math_app.multiply([], 3)
    with pytest.raises(TypeError, match="Input values must be numbers."):
        math_app.divide(10, {})
