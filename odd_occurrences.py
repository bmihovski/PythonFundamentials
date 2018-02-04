"""
Write a program that extracts from a given sequence of words all elements that present in it odd number of times
    (case-insensitive).
    Words are given in a single line, space separated.
    Print the result elements in lowercase, in their order of appearance.
Hints
    Use a dictionary (string í int) to count the occurrences of each word (just like in the previous problem).
    Pass through all key-value pairs in the dictionary and append to the results list all keys that have odd value.
    Print the results list.
"""
prog_langs = input().lower().split(' ')
lang_occur = dict()
results = list()

for lang in prog_langs:
    if lang in lang_occur:
        lang_occur[lang] += 1
    else:
        lang_occur[lang] = 1

{results.append(key) for key, value in lang_occur.items() if value % 2 == 1}
print(*results, sep=', ')
