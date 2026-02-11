"""
Assignment 10

Input: Prompt the user to enter their age.
Processing: Classify the age into different categories:
Under 18: Minor
18-65: Adult
Above 65: Senior citizen
Output: Display the category based on the entered age.
==================================
Challenge: Implement error handling to ensure that the user enters a positive integer for the age.
"""

strAge = ""

# input
while not strAge.isdigit():   # challenge
    strAge = input("Enter a non-negative integer for your age: ")

# processing
intAge = int(strAge)
if intAge < 18:
    strStatus = " Minor"
if 18 <= intAge <= 65:
    strStatus = "n Adult"
if intAge > 65:
    strStatus = " Senior Citizen"

# output
print("At age ",intAge," you are a", strStatus, sep="")
