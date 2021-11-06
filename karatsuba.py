"""
Karatsuba Multiplication

A faster, recursive way of multiplying two integers of n-length.
"""

# x = (10^(n/2))a + b
# y = (10^(n/2))c + d
# where a, b, c, d are (n/2)-digit numbers
# ex:
# x = 23 = 20 + 3
# y = 45 = 40 + 5
# a = 2, b = 3, c = 4, d = 5
# x*y = (10^n)ac + (10^(n/2))(ad + bc) + bd

counter = 0


def karatsuba(x, y):
    global counter
    counter += 1
    print(f"{counter}: multiplying {x} and {y}")
    # base case: if len x or len y < 2, return x * y
    if len(str(x)) < 2 or len(str(y)) < 2:
        return x * y
    # splitting should work for any x or y of length > 4
    else:
        n = int(len(str(x)))
        print(f"n: {n}")
        x_half = (len(str(x))) // 2
        y_half = (len(str(y))) // 2
        print(f"x_half: {x_half}, y_half: {y_half}")
        a = int((str(x))[:x_half])
        b = int((str(x))[x_half:])
        c = int((str(y))[:y_half])
        d = int((str(y))[y_half:])
        # what if length of x or y == 3? a or c should be first two digits and set n to 2
        if len(str(x)) == 3:
            n = 2
            a = int((str(x))[:2])
            b = int((str(x))[2])
        if len(str(y)) == 3:
            n = 2
            c = int((str(y))[:2])
            d = int((str(y))[2])
    print(f"a: {a}, b: {b}, c: {c}, d: {d}")
    ac = karatsuba(a, c)  # recursive
    print(f"ac: {ac}")
    bd = karatsuba(b, d)  # recursive
    print(f"bd: {bd}")
    ad_plus_bc = (karatsuba((a + b), (c + d))) - ac - bd  # inner mult is recursive
    print(f"ad_plus_bc: {ad_plus_bc} = {(a + b) * (c + d)} - {ac} - {bd}")
    print(f"product = ({(10**n)}*ac): {((10**n)*ac)} + ({(10**(int(n/2)))}*ad_plus_bc): {((10**(int(n/2)))*ad_plus_bc)} + bd: {bd}")
    return ((10**n)*ac) + ((10**(int(n/2)))*ad_plus_bc) + bd


print(karatsuba(12340000, 34560000), 12340000 * 34560000)
