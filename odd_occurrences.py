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
#Java C# PHP PHP JAVA C java
prog_langs = 'Java C# PHP PHP JAVA C java'.lower().split(' ')
lang_occur = {}

f = map(lambda lang: lang_occur[lang] += 1 prog_langs else lang_occur[lang] = 1, prog_langs)
print(*f)
