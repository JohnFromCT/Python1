"""
Assignment 16

Description: Develop a function called is_prime that takes a positive integer as input and
returns True if it is a prime number, and False otherwise.
=====================================================
Challenge: Optimize the function to handle large input numbers efficiently.
"""

def is_prime(int_val):
    if int_val < 2:
        return False    # 0 and 1 are not prime
    if int_val == 2:
        return True     # 2 is the only even prime
    if  int_val % 2 == 0:
        return False    # all even numbers (except 2) are not prime
    for i in range(3, int(int_val ** 0.5) + 1, 2):
        if int_val % i == 0:  # divide with every odd number from 3 to the square root to see if no remainder
            return False
    return True
# end of function is_prime

strInput = ""
while not strInput.isdigit():
    strInput = input("Enter a non-negative integer to test for prime-ness: ")

if is_prime(int(strInput)):
    print(strInput, "IS prime!")
else:
    print(strInput, "is NOT prime.")
