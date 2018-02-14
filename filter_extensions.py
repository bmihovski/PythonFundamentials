from glob import glob

"""
You will receive a folder called input, with various files with custom extensions.
You may add or remove the files as you wish, but they are the only way to test your code.
Write a program which accepts a single input line from the Console,
holding an extension … like: "txt", "bmp", "rar" etc.
Print the NAMES AND EXTENSIONS of all files, which have the given extension.

Examples

Input
txt

Output
test.000.001.in.txt
test.000.001.out.txt
test.000.002.in.txt
test.000.002.out.txt
"""
FILES_PATH = "./Resources/04. Filter-Extensions/input/"

file_extension = input()
files = list()

files = [file.split('/')[-1] for file in glob(FILES_PATH + '*.' + file_extension)]

print(*files, sep='\n')
