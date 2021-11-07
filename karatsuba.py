"""
Karatsuba Multiplication

A faster, recursive way of multiplying two integers of n-length.
"""

from math import floor, ceil


def karatsuba(x, y):
    if x < 10 and y < 10:
        """
        If x and y are both single-digit integers, use naive multiplication
        to return their product back up the stack.
        """
        return x * y
    else:
        """
        Maximum number of digits of either of the two multiplicands
        i.e. if length(x) = 17 digits and length(y) = 8 digits, then n = 17.
        """
        n = max(len(str(x)), len(str(y)))

        """
        Split each multiplicand into a first half and second half, based on
        x = a * 10^(n/2) + b, and
        y = c * 10^(n/2) + d.
        Calling ceil() biases the split such that for multiplicands with odd numbers
        of digits, the second half will have more digits than the first half.
        This still works even if the multiplicands are of different lengths.
        """
        p = 10**(ceil(n/2))

        """
        Split x into a and b, and y into c and d.
        If x = 1234, then n = 2 and p = 100;
        a = floor(1234 / 100) = floor(12.34) = 12;
        and b = the remainder of 1234 / 100 = 12 R 34 = 34.
        """
        a = floor(x / p)
        b = x % p
        c = floor(y / p)
        d = y % p

        """
        Recursively calculate three products: ac, bd, and ad + bc.
        ad + bc can be calculated by: (a + b) * (c + d) => (ac + ad + bc + bd)
        and then subtracting ac and bd.
        """
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        e = karatsuba((a + b), (c + d)) - ac - bd

        product = ((10**(2*ceil(n/2)))*ac) + ((10**(ceil(n/2)))*e) + bd

        return product


print(karatsuba(8714, 5126) == 8714 * 5126)
