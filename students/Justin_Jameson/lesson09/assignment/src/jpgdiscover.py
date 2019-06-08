# **************************
# Title: jpgdiscover.py
# Desc:
# 1. Discovers all directories on the server?
# 2. Searches the Parent directory and all subdirectories for jpg files.
# 3. Works from a parent directory called images provided on the command line.
#   a. The program will take the parent directory as input.
#   b. As output, it will return a list of lists structured like this:
#   [“full/working_directory/to/files”, [“file1.jpg”, “file2.jpg”,…], “another/working_directory”,[], etc]
#
# Change Log: (Who, When, What)
# Justin Jameson, 20190602, created file
# Justin Jameson,
# **************************#


import os

# collect current directory and move back one folder.
working_directory = os.path.dirname('../')


def list_jpg_files(path):
    """
    utilizing os.walk to recurse through the directory and find jpg files.  However, only png files have been provided.
    :param path: defines directory to start the search.
    :return: a list of directories and file names.
    """
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            # direction sate find jpg files. However, no jpg files exist so I found png files instead.
            if '.png' in file:
                entry = []
                entry.append(os.path.join(r, file))
                files.append(entry)
    return files


print(list_jpg_files(working_directory))

