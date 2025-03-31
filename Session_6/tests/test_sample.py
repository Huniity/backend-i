
from src.session_6.sample import *
from pytest import raises


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_multiply():
    assert multiply(10,10) == 100
    assert multiply(10, 0) == 0

def test_factorial():
    with raises(RecursionError):
        assert factorial(-1) == 5040
