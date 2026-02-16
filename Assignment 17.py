"""
Assignment 17

Description: Develop a function called find_common_elements that takes two lists as input and
returns a new list containing elements that are common to both input lists.
==============================
Challenge: Optimize the function to handle large input lists efficiently.
"""

def find_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1 & set2)

lstA = [1, 2, 3, 4, 5]
lstB = [3, 4, 5, 6, 7]

print(find_common_elements(lstA, lstB))
