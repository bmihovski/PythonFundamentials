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
pyramids = defaultdict(list)
occur = 1

for _ in range(num_lines_to_check, 0, -1):
    input_line = input()
    for i in range(1, len(input_line)):
        if input_line[i - 1] == input_line[i] and i != len(input_line) - 1:
            occur += 1
        else:
            if occur >= 3:
                pyramids[input_line[i - 1]].append(occur)
                occur = 1
            occur = 1

biggest_formation = (sorted(pyramids, key=lambda k: len(pyramids[k]), reverse=True))[0]

for index in range(len(pyramids[biggest_formation]) + 1):
    if index == 0:
        print(biggest_formation)
    else:
        print(biggest_formation * (index * 2 + 1))
