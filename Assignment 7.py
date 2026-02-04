"""
Assignment 7

Input: Prompt the user to enter a year.
Processing: Determine whether the entered year is a leap year or not. A leap year is divisible by 4 but not by 100 unless it is also divisible by 400.
Output: Display whether the entered year is a leap year or not.
===============================================

Challenge: Handle cases where the user enters non-numeric input for the year and provide appropriate error messages.

"""

# define function
def is_diviz(int_num, int_by):
    flt_calc = float(int_num / int_by)
    if flt_calc == int(flt_calc):
        return True
    else:
        return False

strYear = ""    # initialize input variable

while not strYear.isdigit() or int(strYear) < 1:  # Challenge
    strYear=input("Please enter year in AD: ")

intYear = int(strYear)
if is_diviz(intYear, 400):
    print(intYear,"is a leap year (because it's divisible by 400)!")
else:
    if is_diviz(intYear, 4):
        if is_diviz(intYear, 100):
            print(intYear, "is NOT a leap year because it's a century year not divisible by 400!")
        else:
            print(intYear, "is a leap year!")
    else:
        print(intYear, "is NOT a leap year.")
