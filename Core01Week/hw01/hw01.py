""" Homework 1: Control """

from operator import add, sub


def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)


def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return a * a + b * b + c * c - min(a, b, c) ** 2


def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
    i = 1
    result = 0
    while i < n:
        if n % i == 0:
            result = i
        i += 1
    return result


def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result

# This one is really important: in the with_if_statement, if c() evaluates to True, then f()
# will never get a chance to be evaluated; similarly, if c() evaluates to False, then t() will
# never get a chance to be evaluated
# However, in the with_if_function, since it returns a CALL EXPRESSION: [if_function(c(), t(), f())],
# then we must evaluate the operator first, which is [if_function], then we must evaluate three
# operands in sequence next, before doing anything. So, we have to evaluate all the three operands
# which is [c(), t(), f()]. You can also think of this as: we have to first create a new frame
# called the if_function frame, then you have to set the three formal parameters, which are
# [condition, true_result, false_result] to be the value of [c(), t(), f()], which in this process
# you have to evaluate them BEFORE you actually step into the body part of the if_function
# to do anything more

def with_if_statement():
    """
    >>> result = with_if_statement()
    2
    >>> print(result)
    None
    """
    if c():
        return t()
    else:
        return f()


def with_if_function():
    """
    >>> result = with_if_function()
    1
    2
    >>> print(result)
    None
    """
    return if_function(c(), t(), f())


def c():
    "*** YOUR CODE HERE ***"
    return ''


def t():
    "*** YOUR CODE HERE ***"
    print(1)


def f():
    "*** YOUR CODE HERE ***"
    print(2)


# I copied the rules here:
# Pick a positive integer n as the start.
# If n is even, divide it by 2.
# If n is odd, multiply it by 3 and add 1.
# Continue this process until n is 1.
def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    i = 1
    print(n)
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        print(n)
        i += 1
    return i
