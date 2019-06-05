



#Control:
    #boolean operators:
        #1. and evaluates to True only if both operands evaluate to True.
        #If at least one operand is False, then and evaluates to False.

        #2. or evaluates to True if at least one operand evaluates to True.
        #If both operands are False, then or evaluates to False.

        #3. not evaluates to True if its operand evaluates to False.
        #It evaluates to False if its operand evalutes to True.
# It turns out and and or work on more than just booleans (True, False).
# Python values such as 0, None, '' (the empty string), and [] (the empty list)
# are considered false values. All other values are considered true values.

"""
    >>> True and not False or not True and False
    True

"""
# which is the same as (True and (not False)) or ((not True) and False)




# Important: Call Expressions:

# Every call expression requires a set of parentheses delimiting its comma-separated operands.
#
# To evaluate a function call:
#
# Evaluate the operator, and then the operands (from left to right).
# Apply the operator to the operands (the values of the operands).
# If an operand is a nested call expression, then these two steps are applied to that operand in order to evaluate it.


# When Python executes a return statement, the function terminates immediately.
# If Python reaches the end of the function body without executing a return statement,
# it will automatically return None.
#
# In contrast, the print function is used to display values in the Terminal.
# This can lead to some confusion between print and return because calling a function
# in the Python interpreter will print out the function's return value.
#
# However, unlike a return statement, when Python evaluates a print expression,
# the function does not terminate immediately.

# Notice also that print will display text without the quotes, but return will preserve the quotes.

"""
print and return demo:
    def what_prints():
        print('Hello World!')
        return 'Exiting this function.'
        print('61A is awesome!')
    
    >>> what_prints()
    Hello World!
    'Exiting this function.'

"""

