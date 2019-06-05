# note: this is some important notes and code from lectures

# 1. >>> from math import pi
# >>> radius = 10
# >>> area, circ = pi * radius ** 2, 2 * pi * radius
# notice when you type >>> radius = 0;
# then although area and circ are calculated from radius, area and circ will
# not be update to 0. because once you bound area and circ with the value, you
# are done, there are no relationships any more, there are no dependencies.

# 1.1 However, when you define a function named area which has the following code
# >>> def area():
# ...     return pi * radius * radius
# then area and radius has a relationship, when you changed radius, area will
# get update.

# 2. so Dan just taught that there is a built-in python max function
# which is >>>  __builtins__.max, and you will get <built-in function max> in your
# interpreter, I tried that in the PyCharm Console, but it didn't work, I got an
# error: AttributeError: 'dict' object has no attribute 'max'. However, it works
# when I used my Mac's terminal. I didn't do any research on it right now.

# 3. look at the following code:
# >>> f = min
# >>> f = max
# >>> g, h = min, max
# max = g
# you should be very careful that since g = min, then what max will be bound to
# in the last line is not g, but the value of g, which is min. In general, you
# should always get the value of the right hand side of the equation, then bound
# that to the name on the left side of the "="






