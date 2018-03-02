"""
Write a program to find how many times a given string appears in a given text as substring.
The text is given at the first input line. The search string is given at the second input line.
The output is an integer number. Please ignore the character casing. Overlapping between occurrences is allowed.

Examples:
Input
Welcome to the Software University (SoftUni)! Welcome to programming.
Programming is wellness for developers, said Maxwell.
wel

Output
4
"""
input_text = input().lower()
search_text = input().lower()

char_index = 0
occurrences = 0
while char_index != -1:
    char_index = input_text.find(search_text, char_index)
    if char_index != -1:
        char_index += 1
        occurrences += 1

print(occurrences)
