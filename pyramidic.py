# coding=utf-8
from collections import defaultdict

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

for _ in range(num_lines_to_check, 0, -1):
    input_line = input()
    for pyr_sym in input_line:
        if input_line.count(pyr_sym) >= 3:
            pyramids[pyr_sym].append(input_line.count(pyr_sym) * pyr_sym)
            break

for key, value in pyramids.items():
    if key * num_lines_to_check in value:
        print(key)
        print(*pyramids[key], sep='\n')
