import pytest  
from src.session_6.fixtures import Calculator

@pytest.fixture  
def calculator():  
    return Calculator(2, 3) 

def test_add(calculator):  
    assert calculator.add() == 5  
  
  
def test_subtract(calculator):  
    assert calculator.subtract() == -1  
  
  
def test_multiply(calculator):  
    assert calculator.multiply() == 6  
  
  
def test_divide(calculator):  
    assert calculator.divide() == 0.6666666666666666  

def test_square(calculator):
    assert calculator.square() == 4
  
  
def test_divide_by_zero(calculator):  
    calculator.b = 0  
    with pytest.raises(ZeroDivisionError):  
        calculator.divide()

#poetry add --dev coverage pytest-cov
#poetry run pytest --cov 
