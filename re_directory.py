from glob import glob
from pathlib import Path
from shutil import copyfile

"""
You have been tasked to distribute a directory (folder) of files with various extensions to different folders.
The files should be distributed by their file extension.
You need to group all the files, which have the same extension, into a folder named: "{extension} + s"
In other words: all ".txt" files must be put in a folder called "txts".
The resulting folders should be put in a folder "output".
"""
INPUT_DIR_PATH = "./Resources/08. Re-Directory/input/"
OUT_DIR_PATH = "./Resources/08. Re-Directory/output/"

input_files = [in_file.split('/')[-1] for in_file in glob(INPUT_DIR_PATH + '*')]

[Path(OUT_DIR_PATH + fold.rsplit('.')[-1] + 's').mkdir(parents=True, exist_ok=True) for fold in input_files]

[copyfile(INPUT_DIR_PATH + file_name, OUT_DIR_PATH + file_name.rsplit('.')[-1] + 's' + '/' + file_name) for file_name
 in input_files]
