"""
Assignment 19

Description: Develop a function called sort_list that takes a list of numbers as input and
returns a new list containing the same elements sorted in ascending order.
====================================
Challenge: Implement the sorting algorithm without using any built-in sorting functions.
"""

def sort_list(lst_nums):
    int_len = len(lst_nums)
    for i in range(int_len):
        for x in range(0, int_len - 1 - i):
            if lst_nums[x] > lst_nums[x+1]:  # compare above and below, swap if needed
                temp = lst_nums[x]
                lst_nums[x] = lst_nums[x+1]
                lst_nums[x+1] = temp
    return lst_nums

lstNums = [17, 43, 52, 12, 71, 5, 41, 18, 88, 8]

print(sort_list(lstNums))
