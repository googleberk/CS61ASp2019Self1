

# >>> -2
# -2
# >>> print(-2)
# -2
# >>> 'cal'
# 'cal'
# >>> print('cal')
# cal

# so the above code shows the difference of the value of an expression and
# the printed output

# >>> None
# nothing will be shown on the Python Console

# there are three divisions:
# from operator import truediv, floordiv, mod
# >>> 123 / 10 or truediv(123, 10)
# 12.3
# >>> 123 // 10 or floordiv(123, 10)
# 12
# >>> 123 % 10 or mod(123, 10)
# 3

# we now try an interactive mod: which uses python3 -i ex.py
# if we want to try out the doctest, we can use python3 -m doctest -v ex.py,
# -v is for verbose version, will print out quite a lot test:
# see this example below
from operator import floordiv, mod
def exact_divide(n, d):
    # below is called a doctest:
    """
    :param n:
    :param d:
    :return:
    >>> exact_divide(123, 10)
    (12, 3)
    >>> q, r = exact_divide(123, 10)
    >>> q
    12
    >>> r
    3
    """
    return floordiv(n, d), mod(n, d)


# def statements are compound statements
