"""
Assignment 3

Input: Prompt the user to enter their weight in kilograms and height in meters.
Processing: Calculate the BMI using the formula: BMI = Weight / (Height^2).
Output: Display the calculated BMI.
===============================
Challenge: Provide feedback to the user based on their BMI category
    (e.g., underweight, normal weight, overweight, obese).

Note - Additional Challenge: For added usefulness in the United States, this version
       takes input in imperial measurements and converts to metric for calculations
"""

# inputs
flt_lbs = float(input("Enter weight in pounds: "))
int_ft = int(input("Enter height in whole feet: "))
int_inches = int(input("       and how many inches: "))

# processing
if int_inches > 11:  # checks whether inches is valid, offers instructions if out of range
    print("First enter weight. Next, to enter height, enter whole feet then remaining inches. Run program again.")
    exit(1)    #abend

int_inches = int_inches + (int_ft * 12) # convert feet and inches to total inches
flt_meters = float(int_inches * .0254)  # convert total inches to meters
flt_kg = float(flt_lbs * .4535924)      # convert pounds to kilograms

flt_BMI = float(flt_kg / (flt_meters ** 2))  # BMI is kg/(m^2)

# Challenge: show result categories
if flt_BMI < 18.5:
    str_status="UNDERWEIGHT"
if 18.5 <= flt_BMI < 25:
    str_status="NORMAL WEIGHT"
if 25 <= flt_BMI < 30:
    str_status="OVERWEIGHT"
if 30 <= flt_BMI < 35:
    str_status="MODERATELY OBESE"
if 35 <= flt_BMI < 40:
    str_status="SEVERELY OBESE"
if flt_BMI >= 40:
    str_status="MORBIDLY OBESE"

# output
print ("BMI =", flt_BMI,"  This is considered", str_status)
