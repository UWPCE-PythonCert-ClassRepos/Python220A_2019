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
import logging


def logger_decorator(original_function):
    # import logging
    log_format = "%(asctime)s:%(lineno)-4d %(levelname)s %(message)s"

    # Write to file
    # file_name = 'test_log.log'
    # logging.basicConfig(level=logging.DEBUG, format=log_format,
    #                     filename=file_name)

    # Write to console
    logging.basicConfig(level=logging.DEBUG, format=log_format)

    def wrapper(*args):
        logging.info(
            'Ran {} with args: {}'.format(
                original_function.__name__, args))
        # logging.info(original_function(*args))
        return original_function(*args)

    return wrapper


@logger_decorator
def search_files1(directory='', extension=''):
    extension = extension.lower()
    for dirpath, dirnames, files in os.walk(directory):
        for name in files:
            if extension and name.lower().endswith(extension):
                print(os.path.join(dirpath, name))
            elif not extension:
                print(os.path.join(dirpath, name))


@logger_decorator
def search_files2(directory='', extension=''):
    extension = extension.lower()
    for dirpath, dirnames, files in os.walk(directory):
        logging.debug(f'Directory {dirpath}, Dir Names {dirnames}, Files {files}')
        for name in files:
            logging.debug(f'File Name: {name}')
            if name.lower().endswith(extension):
                print(os.path.join(dirpath, name))


# This includes directories
@logger_decorator
def search_files3(directory='', extension=''):
    extension = extension.lower()
    for root, directories, filenames in os.walk(directory):
        for directory in directories:
            print(os.path.join(root, directory))
        for filename in filenames:
            print(os.path.join(root, filename))


if __name__ == '__main__':

    # search_files1('../images/', '.png')
    search_files2('../images/', '.png')
    # search_files3('../images/', '.png')

