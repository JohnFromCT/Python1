"""
Assignment 5

Input: Prompt the user to enter a time duration in hours.
Processing: Convert the time duration to minutes and seconds.
Output: Display the converted time duration in minutes and seconds.
=======================================================

Challenge: Implement error handling to ensure that the user enters a non-negative number for the time duration.
"""

# input
flt_hours=float(input("Enter a decimal time value in fractional hours: "))

# challenge
if flt_hours < 0:
    print("Value entered must be non-negative!")
    exit(1)  # abend because we didn't learn loops by week 2  lol

# processing
int_seconds = int(flt_hours * 3600)             # converting hours into seconds, dropping off any fractions of seconds
int_minutes = int(int_seconds / 60)             # finds whole minutes, dropping off remainder
int_seconds = int_seconds - (int_minutes * 60)  # changes seconds to remaining seconds after subtracting whole minutes

# output
print(flt_hours,"hours is approximately equal to", int_minutes, "minutes and", int_seconds, "seconds.")