from Test.mathematic import square
import pytest

def test_negative_mathematic():
    assert square(-3) == 9
    assert square(-2) == 4
    assert square(-1) == 1

def test_positive_mathematic():
    assert square(1) == 1
    assert square(2) == 4
    assert square(3) == 9

def test_zero_mathematic():
    assert square(0) == 0

def test_str_argument():
    with pytest.raises(TypeError):
        square("dog")