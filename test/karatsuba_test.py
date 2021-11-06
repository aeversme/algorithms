import pytest
from random import randint
from karatsuba import karatsuba

input_data = [(87, 52), (12340000, 34560000), (8714, 5267)]
# implement a random integer generator function that accepts input n for integer length


def test_karatsuba_small_input():
    x, y = input_data[0]
    print(f"Expected result: {x * y}")
    product = karatsuba(x, y)
    assert product == x * y


def test_karatsuba_large_input():
    x, y = input_data[1]
    print(f"Expected result: {x * y}")
    product = karatsuba(x, y)
    assert product == x * y


def test_karatsuba_uneven_input():
    x, y = input_data[2]
    print(f"Expected result: {x * y}")
    product = karatsuba(x, y)
    assert product == x * y
