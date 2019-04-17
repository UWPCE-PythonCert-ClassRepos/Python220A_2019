"""
I am a.py in students/kevin_cavanaugh/lessons/lesson01/assignment/src
"""

from .b import print_mess
from .c import show_mess


def main():
    '''
    this main function prints letters
    :return:
    '''
    print("in A")
    print_mess("BBBBBB")
    show_mess("CCCCC")


if __name__ == "__main__":
    main()
