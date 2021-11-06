import pytest
from karatsuba import karatsuba


def test_karatsuba_small():
    x = 87
    y = 52
    product = karatsuba(x, y)

    assert product == 4524


def test_karatsuba_large():
    x = 12340000
    y = 34560000
    product = karatsuba(x, y)

    assert product == 426470400000000


def test_karatsuba_uneven():
    x = 8714
    y = 5267
    product = karatsuba(x, y)

    assert product == 45896638
