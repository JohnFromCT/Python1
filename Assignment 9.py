"""
Assignment 9

Input: Ask the user to enter a single character.
Processing: Determine whether the entered character is a vowel (a, e, i, o, u) or a consonant.
Output: Display whether the entered character is a vowel or a consonant.
=====================================================
Challenge: Ensure that the user enters only a single character and handle cases where the input is not a letter.

My additional challenge: check to confirm entry is a letter, with a special check for Y
"""

# define and initialize variables
t_vowels = ("A", "E", "I", "O", "U")  # "Y" is almost never a vowel when the first letter of a word

boolDone= False

while not boolDone:
    strInp = input("Enter a single character: ")
    if len(strInp) == 0:
        print("You only pressed Enter. Try again.")
    elif len(strInp) > 1:
        print("You entered multiple characters. Please only enter one.")
    else:
        boolDone = True

strChar = strInp[0].upper()  # .upper() must be used to conver input to uppercase to match list
if strChar in t_vowels:
    print(strChar,"is a vowel.")
elif strChar == "Y":
    print("Oooh! Sometimes Y!")
elif not strChar.isalpha():
    print(strChar, "isn't even a letter.")
else:
    print(strChar,"is a consonant.")
