"""
Write a program to read a list of integers and find how many odd items it holds.
Hints:
    You can check if a number is odd if you divide it by 2 and check whether you get a remainder of 1.
    Odd numbers, which are negative, have a remainder of -1.
"""
nums_odd = list()
nums_stdin = list(map(int ,input().split(' ')))
[nums_odd.append(item) for item in nums_stdin if item % 2 == 1 or item % 2 == -1]
print(len(nums_odd))
