"""Assignment 14
Description: Develop a function named power that takes two integers, base and exponent, as input and
returns base raised to the power of exponent.
====================================
Challenge: Handle negative exponents efficiently.
"""

# define function
def power(int_base, int_exp):
    return (int_base ** int_exp)

def is_int(str_val):
    try:
        int(str_val)
        return True
    except ValueError:
        return False

strInput = ""
while not is_int(strInput):
    strInput = input("Please enter an integer for the base    : ")
intBase = int(strInput)

strInput = ""
while not is_int(strInput):
    strInput = input("Please enter an integer for the exponent: ")
intExp = int(strInput)

print(intBase, "^", intExp, "=", power(intBase, intExp))
