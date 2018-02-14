"""
Write a program that reads a text file and inserts line numbers in front of each of its lines.
The result should be written to another text file.

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
1. Two house holds, both a like in dignity,
2. In fair Verona, where we lay our scene,
3. From ancient grudge break to new mutiny,
4. Where civil blood makes civil hands unclean.
5. From forth the fatal loins of these two foes
6. A pair of star-cross'd lovers take their life;
7. Whose miss adventured piteous overthrows
8. Do with their death bury their parent's strife.
"""
FILES_PATH = "./Resources/02. Line Numbers/"

file_lines = list()
with open(FILES_PATH + 'Input.txt') as input_file:
    file_lines = input_file.readlines()
    with open(FILES_PATH + 'Output.txt', 'w') as output_file:
        output_file.writelines([f'{index + 1}. {out}' for index, out in enumerate(file_lines)])
