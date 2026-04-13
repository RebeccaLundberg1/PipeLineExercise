import pytest
from src.calculator import Calculator


def test_add():
    calc = Calculator()
    assert calc.add(2, 2) == 4


def test_add_handle_negative_input():
    calc = Calculator()
    assert calc.add(2, -2) == 0


def test_substract():
    calc = Calculator()
    assert calc.subtract(2, 2) == 0


def test_multiply():
    calc = Calculator()
    assert calc.multiply(5, 0) == 0


def test_divide():
    calc = Calculator()
    assert calc.divide(10, 2) == 5


def test_divide_with_negative():
    calc = Calculator()
    assert calc.divide(10, -2) == -5


def test_divide_with_float():
    calc = Calculator()
    assert calc.divide(10, 0.5) == 20


def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError) as e:
        calc.divide(10,0)
    print(e.value)
