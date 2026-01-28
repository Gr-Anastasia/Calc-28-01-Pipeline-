import pytest
from calc import multiplication


def test_multiplication_1():
    assert multiplication(3, 10) == 30

def test_multiplication_2(a,b):
    assert multiplication(3, 10) == 40