# coding=utf-8
from collections import defaultdict
from operator import itemgetter

"""
You will be given N - an integer. On the next N input lines, you will be given N strings,
which may consist of any ASCII character.
Your task is to find the BIGGEST pyramid formation of occurrences of a SINGLE CHARACTER, throughout the strings.
The pyramid is formed by finding a character on a line, then finding 3 consecutive (next to each, other) occurrences of
the same character on the next line, then finding 5 consecutive occurrences on the next line and so on. . .

Example:
abacd
bbbcd
bbbbb
Result:
b
bbb
bbbbb
Check the examples for more info.

Examples

Input
5
asdfghjkl
asdgggjkl
asgggggkl
agggggggl
ggggggggg

7
abcdefg
aaadc\\
cbaaaaa
d
ddddasd
!!ddddd!!!!!!!!...
dddddddd

Output
g
ggg
ggggg
ggggggg
ggggggggg
d
ddd
ddddd
ddddddd
"""
num_lines_to_check = int(input())
pyramids = dict()
input_lines = list()
occur = 1

for _ in range(num_lines_to_check, 0, -1):
    input_line = input()
    input_lines.append(input_line)
    for letter in set(input_line):
        if letter in pyramids:
            letter_count = input_line.count(letter) + pyramids[letter]
            pyramids[letter] = letter_count
        else:
            pyramids[letter] = input_line.count(letter)

if len(pyramids.values()) > 0:
    biggest_formation = (sorted(pyramids, key=pyramids.get, reverse=True))[0]
    row_to_print = 0
    for input_row in input_lines:
        letters_per_row_count = 2 * row_to_print + 1
        letter_per_row_str = str(biggest_formation) * letters_per_row_count
        replaced_row = input_row.replace(letter_per_row_str, ' ')
        if replaced_row == input_row:
            continue
        else:
            row_to_print += 1

for row in range(row_to_print):
    repeat_number = 2 * row + 1
    print(biggest_formation * repeat_number)
