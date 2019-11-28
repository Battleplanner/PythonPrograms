import os
import glob

file_list = glob.glob("./**/*.json", recursive = True)

for file_path in file_list:
    try:
        os.remove(file_path)
    except OSError:
        print("Error while deleting file '{}'".format(file_path))