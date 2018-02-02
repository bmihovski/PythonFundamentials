"""
You will be given a single string, containing random ASCII character.
Your task is to print every character, and how many times it has been used in the string.
"""
acii_str = input()
str_occur = dict()

for char in acii_str:
    if char in str_occur:
        str_occur[char] += 1
    else:
        str_occur[char] = 1

{print(f'-> {value}'): print(f'{key}', end=' ') for key, value in str_occur.items()}
