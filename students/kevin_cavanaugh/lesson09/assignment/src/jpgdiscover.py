"""
assignment 9
jpg recursion program
-discovers jpg files in nested directories
"""

import os


def find_jpg_files(directory):
    """
    looks thru nested directories looking for jpg files
    returns a list of lists for the path of the files found
    """
    list_of_paths = []
    for root, directories, files in os.walk(directory):
        list_of_files = []
        for file in files:
            if '.png' in file:
                list_of_files.append(file)
            if list_of_files:
                list_of_paths.append(root)
                list_of_paths.append(list_of_files)
            for dir in directories:
                find_jpg_files(dir)
        return list_of_paths


def main():
    """
    main
    """
    JPGS = find_jpg_files(os.getcwd())
    for jpg in JPGS:
        print(jpg)


if __name__ == "__main__":
    main()
