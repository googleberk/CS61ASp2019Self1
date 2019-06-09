# 1. Higher-order function: A function that takes a function as an argument value
# or A function that returns a function as a return value.
# Basically, higher order function means function as input or output


def square(x):
    return x ** 2


def apply_twice(f, x):
    """returns the result of calling f twice
    >>> apply_twice(square, 2)
    16


    """
    return f(f(x))


identity = lambda x: x


def make_repeater_recursion(f, n):
    if n == 0:
        return identity
    else:
        def h(x):
            return f(make_repeater_recursion(f, n - 1)(x))

        return h


print(make_repeater_recursion(square, 3)(5))


def make_repeater_loops(f, n):
    def h(x):
        i = 1
        while i <= n:
            x = f(x)
            i += 1
        return x

    return h


print(make_repeater_loops(square, 3)(5))
