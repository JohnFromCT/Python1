"""
Assignment 8

Input: Ask the user to enter their marks for three subjects.
Processing: Calculate the average of the marks. Determine the grade based on the average:
90 and above: A
80-89: B
70-79: C
60-69: D
Below 60: F
Output: Display the calculated grade.

=================================================
Challenge: Implement error handling to ensure that the user enters valid marks (between 0 and 100) for each subject.

"""
intClasses = 3   # hard-coding number of classes to average

# inputs
intGrade = 0
for intCount in range(intClasses):
    strInput="x"
    while not strInput.isdigit() or int(strInput) > 100:  # Challenge
        print("Enter percentage score for class", intCount+1, "(0 to 100): ")
        strInput = input()
    intGrade = intGrade + int(strInput)  # adds to intGrade the sum of all grades

# processing
intGrade = int(intGrade / intClasses)    # division will yield a float, but this can be truncated

# output
if intGrade < 60:
    print("Grade:", intGrade, "% = F")
if 60 <= intGrade < 70:
    print("Grade:", intGrade, "% = D")
if 70 <= intGrade < 80:
    print("Grade:", intGrade, "% = C")
if 80 <= intGrade < 90:
    print("Grade:", intGrade, "% = B")
if intGrade >= 90:
    print("Grade:", intGrade, "% = A")

