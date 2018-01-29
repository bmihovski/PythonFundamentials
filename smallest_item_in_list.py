"""
Write a program to read a list of integers, find the smallest item and print it.
Hints
Loop through the integer list until you find the smallest item
"""

nums_to_check = input().split(' ')
nums = list()
[nums.append(int(item)) for item in nums_to_check]
print(min(nums))
