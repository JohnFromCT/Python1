"""
Assignment 15

Description: Create a function named is_palindrome that takes a string as input and returns
True if it is a palindrome, and False otherwise.
===================================
Challenge: Write the function using recursion.
"""

def is_palindrome(str_string):
    intLen = len(str_string)
    strCompare = str_string.upper()  # converts to all uppercase to make comparison not case sensitive

    for intIndex in range(0, int(intLen / 2)):  # truncates if odd, does not need to compare middle character
        intCountback = len(strCompare) - (intIndex + 1)
        if strCompare[intIndex] != strCompare[intCountback]:
            return False
    return True

strInput = input("Enter a string: ")

if is_palindrome(strInput):
    print(strInput, "IS a palindrome!")
else:
    print(strInput, "is NOT a palindrome.")