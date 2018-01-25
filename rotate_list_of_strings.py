"""
Write a program to read a list of strings, rotate it to the right and print its rotated items.
Hints
    You can store the rotated list in a second list alongside the first one
"""
list_of_strings = input().split(' ')
print(*reversed(list_of_strings))
