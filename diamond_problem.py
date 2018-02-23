from string import digits

"""
In the programming languages, which permit multiple inheritance, the diamond problem is a very common problem.
In our task, the diamond problem is a bit more… money driven.
Your task is to write a program, which finds all diamonds in a string and calculates the carats of each diamond.
Each diamond will start with the character '<'.
After that, it will be followed by several random characters (contents of the diamond).
The diamond will end with the character '>'.
The carat value of the diamond is equal to the sum of all the digits in the contents of the diamond.
Example: "<2big32diamond>"  2 + 3 + 2  7 carats
If the given string contains one or more diamonds, print for each found diamond the following output:
Found {caratValueOfTheDiamond} carat diamond
If in the given string cannot be found any diamond, print:
Better luck next time

Input
empty<2big32diamond>useless<1another02Diamond>
No>diamonds<here
No>diam<55onds><here

Output
Found 7 carat diamond
Found 3 carat diamond
Better luck next time
"""
input_text = input()
allowed_chars = digits + '<>'


def find_all_starting_indexes(filtered_str):
    """
    Calculates start indexes of diamonds
    :param filtered_str: (Str) Diamonds separated by '<>'
    :return: (List) Diamonds '<' Indexes from filtered_str
    """
    diamond_indexes = list()
    last_index = 0
    while True:
        index = filtered_str.find('<', last_index)
        if index == -1:
            break
        diamond_indexes.append(index)
        last_index = index + 1
    return diamond_indexes


filtered_str = ''.join(filter(lambda x: x in allowed_chars, input_text))

diamonds_with_indexes = find_all_starting_indexes(filtered_str)

diamonds = list()

for start_index in diamonds_with_indexes:
    end_index = filtered_str.find('>', start_index)
    if end_index == -1:
        continue
    diamond_str = filtered_str[start_index + 1: end_index]
    diamond_value = sum([int(char) for char in diamond_str])
    diamonds.append(diamond_value)

if diamonds:
    [print(f'Found {carat} carat diamond') for carat in diamonds]
else:
    print('Better luck next time')
