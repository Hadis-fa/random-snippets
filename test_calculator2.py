# instead we can use pytest to test our code
# in order to use this package you need to install it first using pip install pytest and then run pytest "name of our file"
from calculator import square
import pytest



def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")
        
