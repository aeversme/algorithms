import pytest
from karatsuba import karatsuba

input_data = [(87, 52), (12340000, 34560000), (8714, 5267)]


def test_karatsuba_small_input():
    x, y = input_data[0]
    product = karatsuba(x, y)
    assert product == 4524


def test_karatsuba_large_input():
    x, y = input_data[1]
    product = karatsuba(x, y)
    assert product == 426470400000000


def test_karatsuba_uneven_input():
    x, y = input_data[2]
    product = karatsuba(x, y)
    assert product == 45896638
