"""
Assignment 18

Description: Create a function called concat_tuples that takes two tuples as input and
returns a new tuple containing all elements from both input tuples.
=============================================
Challenge: Ensure that the function works correctly with tuples of different lengths.
"""

def concat_tuples(tuple1, tuple2):
    return tuple1 + tuple2

# Example with different lengths
t1 = (1, 2)
t2 = (3, 4, 5, 6)
tresult = concat_tuples(t1, t2)
print(tresult)
