"""
Assignment 12

Description: Develop a program that prompts the user to enter the number of rows for a pattern and then prints a
pattern of asterisks (*) in the form of a right triangle.
=========================================
Challenge: Use nested loop structures to print the pattern efficiently and neatly. Allow the user to specify the
character used for the pattern.
"""

strInput = ""
while not strInput.isdigit():
    strInput = input("Enter the side length of the equilateral right triangle: ")

intNum = int(strInput)
if intNum > 45:
    print("Nope.  I don't want to make it so big!  Run again with 45 or less.")
    exit(1)

strInput = ""
while len(strInput) != 1:
    strInput = input("Enter a character to be used: ")
    if len(strInput) == 0:
        print("You only pressed Enter. Try again.")
    elif len(strInput) > 1:
        print("You entered more than one character. Please only enter one.")

for intSide in range(intNum, 0, -1):
    for intRow in range(0, intSide):
        print(strInput[0],end="")
    print("")

