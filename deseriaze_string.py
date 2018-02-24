"""
Write a program, which takes the output from the previous task and turns it back into a string.
Until you receive the line "end", you will receive several lines of input on the console, in the following format:
"	{letter}:{index1}/{index2}/{index…}/{indexN}
Your task is to take every letter and its index and form a string out of them.

Examples

Input
a:0/2/4/6
b:1/3/5
end

a:0/3/5/11
v:1/4
j:2
m:6/9/15
s:7/13
d:8/14
c:10
l:12
end

Output
abababa
avjavamsdmcalsdm
"""
char_collection = dict()
deserialize_chars = list()

while True:
    input_string = input()
    if 'end' in input_string:
        break
    get_dict_value = input_string.partition(':')
    [char_collection.update({int(key): get_dict_value[0]}) for key in get_dict_value[-1].split('/')]

for key in sorted(char_collection.keys()):
    deserialize_chars.append(char_collection[key])

print(''.join(deserialize_chars))
