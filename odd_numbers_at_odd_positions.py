"""
Write a program to read a list of integers and find how many odd numbers at odd positions the list holds.
If there are no numbers, which match this criterion, do not print anything
Hints
  Positions are counted from 0 from left to right, so if for example the second item (index 1) is odd,
  then we should count it, and so on…
  Do NOT count odd numbers, which are at even positions (0, 2, 4, etc…)
"""
nums_to_check = list(map(int, input().split(' ')))
[print(f'Index {c} -> {item}') for c, item in enumerate(nums_to_check) if c % 2 != 0 and item % 2 != 0]
