"""
Write a program to append several lists of numbers.
    Lists are separated by '|'.
    Values are separated by spaces (' ', one or several)
    Order the lists from the last to the first, and their values from left to right.
Hints
    Create a new empty list for the results.
    Split the input by '|' into list of tokens.
    Pass through each of the obtained tokens from tight to left.
        For each token, split it by space and append all non-empty tokens to the results.
    Print the results.
"""
tokens = input().split('|')
tokens.reverse()
results = [print(*item.split(), end=' ') for nums in tokens for item in nums.split()]
