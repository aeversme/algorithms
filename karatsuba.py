"""
Karatsuba Multiplication
"""

# x = (10^(n/2))a + b
# y = (10^(n/2))c + d
# where a, b, c, d are (n/2)-digit numbers
# ex:
# x = 23 = 20 + 3
# y = 45 = 40 + 5
# a = 2, b = 3, c = 4, d = 5
# x*y = (10^n)ac + (10^(n/2))(ad + bc) + bd


def karatsuba(x, y):
    # base case: if len x or len y < 2, return x * y
    # splitting should work for any odd x or y of length > 4
    # what if length of x or y == 3? a or c is first two digits
    n = int(len(str(x)))
    x_half = (len(str(x)))//2
    y_half = (len(str(y)))//2
    print(x_half, y_half)
    a = int((str(x))[:x_half])
    b = int((str(x))[x_half:])
    c = int((str(y))[:y_half])
    d = int((str(y))[y_half:])
    print(a, b, c, d)
    ac = a * c  # recursive
    bd = b * d  # recursive
    ad_plus_bc = ((a + b)*(c + d)) - ac - bd  # inner mult recursive
    return ((10**n)*ac) + ((10**(int(n/2)))*ad_plus_bc) + bd


print(karatsuba(87, 39))
