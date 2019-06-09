from math import pi, sqrt


def area_square(r):
    """Return the area of a square with side length R."""
    # see how this assert works:
    assert r >= 0, "R needs to be non-negative"
    return r * r


def area_circle(r):
    """Return the area of a circle with side radius R."""
    return r * r * pi


def area_hexagon(r):
    """Return the area of a regular hexagon with side length R."""
    return r * r * 3 * sqrt(3) / 2


# print(area_square(10))

# the problem with the code above is that you are repeating yourself, so you
# need to generalize your code in the way below:
def area(r, shape_constant):
    """Return the area of a shape from length measurement R."""
    assert r >= 0, "R needs to be non-negative"
    return r * r * shape_constant


def area_square(r):
    return area(r, 1)


def area_circle(r):
    return area(r, pi)


def area_hexagon(r):
    return area(r, 3 * sqrt(3) / 2)


# below is about higher order functions:

def cube(k):
    return pow(k, 3)


def identity(k):
    return k


def pi_term(k):
    return 8 / ((4 * k - 3) * (4 * k - 1))


# this is a higher order function because term is a function of k
def summation(n, term):
    """Sum the first N terms of a sequence"""
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total


print(summation(1000000, pi_term))


# locally defined functions:

def make_adder(n):
    """Return a function that takes one argument k and returns k + n"""

    def adder(k):
        return k + n

    return adder


print(make_adder(3)(5))
