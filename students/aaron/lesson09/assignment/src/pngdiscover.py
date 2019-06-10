#!/usr/bin/env python3
''' A simple recursive png discoverer '''

import argparse
import os

def parse_cmd_arguments():
    """
    Parses cli arguments
    """
    parser = argparse.ArgumentParser(description='Find some images.')
    parser.add_argument('-i', '--images', help='images path', required=True)
    return parser.parse_args()

def list_png_files(path):
    ''' Recursively finds files in (path) '''
    locations = os.listdir(path)
    files = []
    my_files = []
    # the locations must be sorted to reliably pass the test
    for location in sorted(locations):
        full_name = os.path.join(path, location)
        # if location is a file and ends in .png, append it
        if os.path.isfile(full_name) and full_name[-4:].lower() == '.png':
            if my_files:
                my_files[1].append(location)
            else:
                my_files = [path, [location]]
        # if location is a directory, recurse and append the results
        if os.path.isdir(full_name):
            sub_files = list_png_files(full_name)
            # only append if not empty
            if sub_files:
                files += sub_files
    # prunes empty dirs
    if my_files:
        return my_files + files
    return files

# process cli args when called outside of tests
if __name__ == "__main__":
    ARGS = parse_cmd_arguments()
    if not os.path.isdir(ARGS.images):
        print("ERROR: The path %s is not a directory or does not exist." % ARGS.images)
        exit()
    print(list_png_files(ARGS.images))
