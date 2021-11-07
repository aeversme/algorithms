import pytest
from random import randint
from karatsuba import karatsuba


def random_integers(n):
    lower = 10**(n-1)
    upper = 10**n - 1
    return randint(lower, upper), randint(lower, upper)


def uneven_integers(n):
    lower = 10**(n-3)
    upper = 10**(n+6) - 1
    return randint(lower, upper), randint(lower, upper)


def test_karatsuba_small_input():
    x, y = random_integers(7)
    print(f"Expected result: {x * y}")
    assert karatsuba(x, y) == x * y


def test_karatsuba_large_input():
    x, y = random_integers(27)
    print(f"Expected result: {x * y}")
    assert karatsuba(x, y) == x * y


def test_karatsuba_uneven_input():
    x, y = uneven_integers(15)
    print(f"Expected result: {x * y}")
    assert karatsuba(x, y) == x * y
