# Print out 2 to the 65536 power
# (try doing the same thing in the JS console and see what it outputs)

import math

# YOUR CODE HERE

print(2 ** 65536)

# V2:
# Doesn'tt work because in Python floating point numbers are not arbitrary large. Only ints are
# https://stackoverflow.com/a/43149008/1368742
# print((math.pow(2, 65536)))

# JS:
# console.log(Math.pow(2, 65536)) # Infinity
# console.log(2 ** 65536) # Infinity
