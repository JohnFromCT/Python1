"""
Input: Ask the user to enter the length and width of a rectangle.
Processing: Calculate the area of the rectangle using the formula: Area = Length * Width.
Output: Display the calculated area of the rectangle.
=================================
Challenge: Implement error handling to ensure that the length and width entered by
the user are positive numbers.
"""

#inputs
flt_len = float(input("Enter the length of the rectangle: "))
flt_width = float(input("Enter the width of the rectangle: "))

#challenge: confirm user input is within valid range, will abort if negative
if flt_len < 0 or flt_width < 0:
    print("Negative values are invalid!")
    exit(1)

#processing
flt_area = flt_len * flt_width

#output
print ("The area of this rectangle is", flt_area)