"""
Karatsuba Multiplication

A faster, recursive way of multiplying two integers of n-length.
"""

from math import floor, ceil


def karatsuba(x, y):
    if x < 10 and y < 10:
        return x * y
    else:
        n = max(len(str(x)), len(str(y)))
        p = 10**(ceil(n/2))

        a = floor(x / p)
        b = x % p
        c = floor(y / p)
        d = y % p

        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        e = karatsuba((a + b), (c + d)) - ac - bd

        product = ((10**(2*ceil(n/2)))*ac) + ((10**(ceil(n/2)))*e) + bd

        return product


print(karatsuba(1234567890123456789, 9876543) == 1234567890123456789 * 9876543)
