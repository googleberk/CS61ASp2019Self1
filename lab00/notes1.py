
# The lines in the triple-quotes """ are called a docstring,
# which is a description of what the function is supposed to do.
"""
in python: 7/2 = 3.5, and 7//2 = 3.

>>> 7 /2
3.5

>>> 7 // 2
3
"""

# Programs are made up of expressions and statements.
# In very simple terms, an expression is a piece of code that
# evaluates to some value and a statement is one or more lines
# of code that make something happen in a program

# Primitive expressions only take one step to evaluate.
# These include numbers and booleans, which just evaluate to themselves.
# Names are also primitive expressions. Names evaluate to the value that
# they are bound to in the current environment.
# One way to bind a name to a value is with an assignment statement.

"""
An assignment statement consists of a name and an expression. 
It changes the state of the program by evaluating the expression and binding its value to the name in the current frame.

>>> a = (100 + 50) // 2
Note that the statement itself doesn't evaluate to anything, because it's a statement and not an expression. 
Now, if we ask for a's value, the interpreter will look it up in the current environment and output its value.

>>> a
75

Note that the name a is bound to the value 75, not the expression (100 + 50) // 2. 
Names are bound to values, not expressions.


"""

















