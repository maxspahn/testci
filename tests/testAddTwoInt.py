import pytest
from simpleOperators.addTwoInt import add

def test_1plus1():
    a = 1
    b = 1
    res = add(a, b)
    assert res == 2

def test_2plus1():
    a = 2
    b = 1
    res = add(a, b)
    assert res == 3

