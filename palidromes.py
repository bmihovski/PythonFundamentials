"""
Write a program that extracts from a given text all palindromes, e.g. ABBA, lamal, exe
and prints them on the console on a single line, separated by comma and space.
Use space as word delimiter. Print only unique palindromes, sorted lexicographically.

Input
Hi exe ABBA Hog fully a string Bob

Output
a, ABBA, exe
"""

input_words = input().split()

words = filter(lambda x: x == x[::-1], input_words)

print(*sorted(words, key=str.lower), sep=', ')
