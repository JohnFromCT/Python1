"""
Assignment 11

Description: Write a program that generates the Collatz sequence for a given positive integer
entered by the user. The Collatz sequence is generated iteratively by repeatedly applying the following rules:
If the current number is even, divide it by 2.
If the current number is odd, multiply it by 3 and add 1.
Use a loop structure to generate the Collatz sequence until it reaches 1.
=================================
Challenge: Handle cases where the user enters a non-numeric input.
"""

strInput = ""

while not strInput.isdigit() or int(strInput) == 0:   # challenge
    strInput = input("Enter a positive number to start the Collatz sequence: ")

intValue = int(strInput)

while intValue > 1:
    print(intValue, end= " -> ")
    if intValue % 2 == 0:
        intValue = int(intValue/2)
    else:
        intValue = (intValue*3) +1

print("1")
