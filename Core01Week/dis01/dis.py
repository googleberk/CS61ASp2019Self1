

# Question 1.1:
# Alfonso will only wear a jacket outside if it is below 60 degrees or it is raining.
# Write a function that takes in the current temperature and a boolean value telling
# if it is raining and returns True if Alfonso will wear a jacket and False otherwise.

def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    return temp < 60 or raining

# Question 1.3:
# Write a function that returns True if a positive integer n is a prime number and False otherwise.
def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    if n == 1:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True

# back notes: Alternatively, the while loop’s conditional expression could
# ensure that i is less than or equal to the square root of n.




