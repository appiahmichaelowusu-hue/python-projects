import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_multiply(calc):
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(-1, 5) == -5
    assert calc.multiply(0, 10) == 0

def test_add(calc):
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 5) == 4
    assert calc.add(0, 10) == 10

def test_multiply_type_error(calc):
    with pytest.raises(TypeError):
        calc.multiply("hello", 3)

def test_add_type_error(calc):
    with pytest.raises(TypeError):
        calc.add("hello", 3)
