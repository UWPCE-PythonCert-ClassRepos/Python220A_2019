# --------------------------------------------------------------------------- #
# Course: PYTHON 220: Advanced Programming in Python
# Script Title: Lesson 9 Assignment
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-06-03, Initial release
# --------------------------------------------------------------------------- #

# Note: Run with 'python src/image_discover_01.py' from Assignment directory
# via Command Prompt

import argparse
from argparse import RawTextHelpFormatter

import os


def logger_decorator(original_function):
    import logging as l
    log_format = "%(asctime)s:%(lineno)-4d %(levelname)s %(message)s"

    args = parse_cmd_arguments()

    if args.debug == 'console':
        l.basicConfig(level=l.DEBUG,
                      format=log_format)

    elif args.debug == 'file':
        file_name = 'HPNorton_log.txt'
        l.basicConfig(level=l.DEBUG,
                      format=log_format,
                      filename=file_name)

    else:
        l.basicConfig(level=l.CRITICAL)

    def wrapper(*args):
        l.info('Function %s ran with args: %s', original_function.__name__, args)
        original_function_output = original_function(*args)
        l.info('Function Output:')

        for path, files in original_function_output.items():
            l.info('\tIn Directory: %s', path)
            l.info('\t\tFound Files: %s', files)

        return original_function(*args)

    return wrapper


def parse_cmd_arguments():
    """
    Parse command line arguments
    :return:
    """
    parser = argparse.ArgumentParser(description='File Search.',
                                     formatter_class=RawTextHelpFormatter)

    parser.add_argument('-f', '--folder',
                        help='Folder to search',
                        required=True)

    parser.add_argument('-e', '--extension',
                        help='File extension',
                        required=True)

    parser.add_argument('-d', '--debug',
                        help='Debug messages:\n'
                        'disable: Disable\n'
                        'console: Enable to Console\n'
                        'file: Enable to File\n',
                        required=False)

    return parser.parse_args()


@logger_decorator
def search_files(directory='', extension=''):
    extension = extension.lower()
    files_dict = {}

    for dir_path, dir_names, files in os.walk(directory):

        for name in files:
            if name.lower().endswith(extension):
                files_dict[dir_path] = files
    return files_dict


if __name__ == '__main__':
    args = parse_cmd_arguments()
    files_list = search_files(args.folder, args.extension)
