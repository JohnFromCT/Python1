"""
Assignment 13

Description: Write a program that prompts the user to enter a string and then checks whether it is a palindrome.
A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.
===================================
Challenge: Use a loop structure to compare characters from both ends of the string to determine
whether it is a palindrome.
"""

# input
strInput = input("Enter a string: ")

# processing
boolPalindrome = True
intLen = len(strInput)
strCompare = strInput.upper()  # converts to all uppercase to make comparison not case sensitive

for intIndex in range(0, int(intLen/2)): # truncates if odd, does not need to compare middle character
    intCountback = len(strInput) - (intIndex+1)
    if strCompare[intIndex] != strCompare[intCountback]:
        boolPalindrome = False

# output
if boolPalindrome:
    print(strInput, "IS a palindrome!")
else:
    print(strInput, "is NOT a palindrome.")

