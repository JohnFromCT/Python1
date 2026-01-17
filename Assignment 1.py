"""
Assignment 1

Input: Prompt the user to enter the principal amount, interest rate (in percentage),
and the time period (in years).
Processing: Calculate the simple interest using the formula:
Simple Interest = (Principal * Rate * Time) / 100.
Output: Display the calculated simple interest.
"""

#inputs
principal_flt = float(input("Enter the principal amount: $"))
rate_flt = float(input("Enter the interest percentage rate: "))
years_flt = float(input("Enter the time period in years: "))

#processing
interest_flt = principal_flt * rate_flt * years_flt / 100  #compounded only once

#output
print("You will pay back an additional $", interest_flt, "in interest in",
      years_flt, "years for a total of $", principal_flt + interest_flt)
