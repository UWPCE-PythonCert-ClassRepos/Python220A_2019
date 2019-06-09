# --------------------------------------------------------------------------- #
# Course: PYTHON 220: Advanced Programming in Python
# Script Title: Lesson 9 Assignment
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-06-03, Initial release
# --------------------------------------------------------------------------- #

# The program will take the parent directory as input. As output, it will
# return a list of lists structured like this: [“full/path/to/files”,
# [“file1.jpg”, “file2.jpg”,…], “another/path”,[], etc]

# Note: Run with 'python src/image_discover_01.py' from Assignment directory
# via Command Prompt

# TODO: Use decorators for logging
# TODO: Add cmd argument parser (see A02)

import argparse
from argparse import RawTextHelpFormatter

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
def parse_cmd_arguments():
    """
    Parse command line arguments
    :return:
    """
    parser = argparse.ArgumentParser(description='File Search.',
                                     formatter_class=RawTextHelpFormatter)

    parser.add_argument('-f', '--folder', help='Folder to search', required=True)
    parser.add_argument('-e', '--extension', help='File extension',
                        required=True)

    parser.add_argument('-d', '--debug', help='Debug message level:\n'
                                              '0: No debug messages or '
                                              'log file\n'
                                              '1: Only error messages\n'
                                              '2: Error messages and warnings\n'
                                              '3: Error messages, warnings,'
                                              'and debug messages',
                        required=False)

    return parser.parse_args()


# @logger_decorator.
def search_files(directory='', extension=''):
    extension = extension.lower()
    images = {}
    for dirpath, dirnames, files in os.walk(directory):

        l.debug(f'Directory {dirpath}, Dir Names {dirnames}, Files {files}')
        l.debug(f'Directory {type(dirpath)}, Dir Names {type(dirnames)}, Files {type(files)}')

        for name in files:
            l.debug(f'File Name: {name}')
            if name.lower().endswith(extension):
                images[dirpath] = files

                l.debug(os.path.join(dirpath, name))

    return images


if __name__ == '__main__':
    args = parse_cmd_arguments()

    image_list = search_files(args.folder, args.extension)
    print(image_list)

