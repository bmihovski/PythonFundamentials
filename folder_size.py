from os import stat, walk

"""
You are given a folder named "TestFolder". Get the size of all files in the folder, which are NOT directories.
The result should be written to another text file in Megabytes.

Examples

Output.txt
5.161738395690918
"""
FILES_PATH = "./Resources/07. Folder Size/TestFolder/"

for root, dirs, files in walk(FILES_PATH):
    sizes = [stat(root + '/' + file).st_size for file in files]
    total_size = sum(sizes)
    total_size_mb = total_size / 1024 / 1024
    open('Output.txt', 'w').write(str(total_size_mb))
