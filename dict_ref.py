"""
You have been tasked to create a referenced dictionary, or in other words a dictionary,
    which knows how to reference itself.
You will be given several input lines, in one of the following formats:
    {name} = {value}
    {name} = {secondName}
The names will always be strings, and the values will always be integers.
In case you are given a name and a value, you must store the given name and its value.
If the name already EXISTS, you must CHANGE its value with the given one.
In case you are given a name and a second name,
you must store the given name with the same value as the value of the second name.
If the given second name DOES NOT exist, you must IGNORE that input.
When you receive the command "end", you must print all entries with their value, by order of input, in the following format:
{entry} === {value}
"""
input_values = dict()
inputs_stdin = list()
while 'end' not in inputs_stdin:
    inputs_stdin = input().split(' = ')
    if 'end' in inputs_stdin:
        continue
    try:
        input_values.update({inputs_stdin[0]: int(inputs_stdin[1])})
    except ValueError:
        if inputs_stdin[1] in input_values:
            input_values.update({inputs_stdin[0]: input_values[inputs_stdin[1]]})
        else:
            continue

{print(f'{key} === {input_values[key]}') for key in input_values.keys()}
