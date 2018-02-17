from fileinput import input

"""
Write a program that reads the contents of two text files and merges them together into a third one.

Examples

Input1.txt
1
3
5

Input2.txt
2
4
6

Output.txt
1
2
3
4
5
6
"""
FILES_PATH = "./Resources/03. Merge Files/"

file_names = [FILES_PATH + 'FileOne.txt', FILES_PATH + 'FileTwo.txt']

with open(FILES_PATH + 'Output.txt', 'w') as output_file, input(file_names) as input_files:
    input_files = [new_line + '\n' if new_line[-1] != '\n' else new_line for new_line in sorted(input_files)]
    [output_file.write(line) for line in input_files]
