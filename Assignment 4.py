"""
Assignment 4

Input: Prompt the user to enter the coordinates of two points in a 2D plane (x1, y1) and (x2, y2).
Processing: Calculate the distance between the two points using the distance formula: Distance = sqrt((x2 - x1)^2 + (y2 - y1)^2).
Output: Display the calculated distance between the two points.
"""

# input
flt_x1 = float(input("Enter X value of first coordinate: "))
flt_y1 = float(input("Enter Y value of first coordinate: "))
flt_x2 = float(input("Enter X value of second coordinate: "))
flt_y2 = float(input("Enter Y value of second coordinate: "))

# processing
flt_dist = (((flt_x1 - flt_x2) ** 2) + ((flt_y1 - flt_y2) ** 2)) ** 0.5

# output
print("Distance between these coordinates is", flt_dist)
