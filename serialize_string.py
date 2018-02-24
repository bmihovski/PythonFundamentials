from collections import defaultdict

"""
You have been tasked to serialize a string. The serialization is done in a special way,
in which a character from that string is saved with the indexes at which it is found.
The input will consist of a single input line, containing a single string, which may consist of ANY ASCII character.
Your task is to serialize the string in the following way:
{char}:{index1}/{index2}/{index3}
The char will be the character, and the indexes, will be the indexes it is found at in the string.
Note: This problem is a string problem, and should ONLY use strings in its solution.

Examples

Input
abababa

avjavamsdmcalsdm

Output
a:0/2/4/6
b:1/3/5

a:0/3/5/11
v:1/4
j:2
m:6/9/15
s:7/13
d:8/14
c:10
l:12
"""
input_string = input()
chars_positions = defaultdict(list)

for i, x in enumerate(input_string):
    chars_positions[x].append(str(i))

for key, value in chars_positions.items():
    positions = '/'.join(value)
    print(f'{key}:{positions}')
