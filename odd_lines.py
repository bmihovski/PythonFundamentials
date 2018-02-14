"""
Write a program that reads a text file and writes its every odd line in another file. Line numbers starts from 0.

Examples

Input.txt
Two house holds, both a like in dignity,
In fair Verona, where we lay our scene,
From ancient grudge break to new mutiny,
Where civil blood makes civil hands unclean.
From forth the fatal loins of these two foes
A pair of star-cross'd lovers take their life;
Whose miss adventured piteous overthrows
Do with their death bury their parent's strife.

Output.txt
In fair Verona, where we lay our scene,
Where civil blood makes civil hands unclean.
A pair of star-cross'd lovers take their life;
Do with their death bury their parent's strife.
"""
FILES_PATH = "./Resources/01. Odd Lines/"

lines = list()
with open(FILES_PATH + 'Input.txt') as input_file:
    lines = input_file.readlines()
    with open(FILES_PATH + 'Output.txt', 'w') as out_file:
        out_file.writelines([line for index, line in enumerate(lines) if index % 2 != 0])
