# --------------------------------------------------------------------------- #
# Course: PYTHON 220: Advanced Programming in Python
# Script Title: Lesson 9 Assignment
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-06-03, Initial release
# --------------------------------------------------------------------------- #

# The program will take the parent directory as input. As output, it will
# return a list of lists structured like this: [“full/path/to/files”,
# [“file1.jpg”, “file2.jpg”,…], “another/path”,[], etc]

import os
import logging as l
from pprint import pprint as print


def logger_decorator(original_function):
    # import logging
    log_format = "%(asctime)s:%(lineno)-4d %(levelname)s %(message)s"

    # Write to file
    # file_name = 'test_log.log'
    # logging.basicConfig(level=logging.DEBUG, format=log_format,
    #                     filename=file_name)

    # Write to console
    l.basicConfig(level=l.DEBUG, format=log_format)

    def wrapper(*args):
        l.info(
            'Ran {} with args: {}'.format(
                original_function.__name__, args))
        # logging.info(original_function(*args))
        return original_function(*args)

    return wrapper


# @logger_decorator
def search_files(directory='', extension=''):
    extension = extension.lower()
    images = {}
    for dirpath, dirnames, files in os.walk(directory):

        # images[dirpath] = files

        l.debug(f'Directory {dirpath}, Dir Names {dirnames}, Files {files}')
        l.debug(f'Directory {type(dirpath)}, Dir Names {type(dirnames)}, Files {type(files)}')

        for name in files:

            images[dirpath] = files

            l.debug(f'File Name: {name}')
            if name.lower().endswith(extension):
                l.debug(os.path.join(dirpath, name))
    return images


if __name__ == '__main__':
    image_list = search_files('../images/', '.png')

    print(image_list)

