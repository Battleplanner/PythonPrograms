import os
import glob

file_list = glob.glob("./**/*.json", recursive = True)

for file_path in file_list:
    try:
        os.remove(file_path)
    except OSError:
        print("Error while deleting file '{}'".format(file_path))

"""
To use:

Make sure the program is in the same folder as the folder containing all the files to be deleted.
It should be placed in the topmost folder, e.g if we want to delete all the json files in folders 'log1' and 'log'2,
we would put the program next to the folder containing these folders.

Keep in mind that this will delete all json files in all folders and subfolders. Make sure that all the data
you want to keep is saved and/or moved somewhere else. I take no responsibility for any damage caused by the program 
not working or running as it should. Use at your own risk.

"""