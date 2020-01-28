# --------------------------------------------------------------------------- #
# Course: PYTHON 220: Advanced Programming in Python
# Script Title: 
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-06-02, Initial release
# --------------------------------------------------------------------------- #


import os
import sys
import src.database


if __name__ == "__main__":

    # new_wd = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    # os.chdir(new_wd)
    cwd = os.getcwd()

    print(cwd)
    print(sys.path)
