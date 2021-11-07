"""
Karatsuba Multiplication

A faster, recursive way of multiplying two integers of n-length.
"""


def karatsuba(x, y):
    if x < 10 and y < 10:
        return x * y
    else:
        n = max(len(str(x)), len(str(y)))
        n2 = n // 2

        a = x // 10 ** n2
        b = x % 10 ** n2
        c = y // 10 ** n2
        d = y % 10 ** n2

        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        e = karatsuba((a + b), (c + d))

        return (ac * 10 ** (2 * n2)) + ((e - ac - bd) * (10 ** n2)) + bd


print(karatsuba(8714, 5126) == 8714 * 5126)
