# ---------------------------------------------------------------------------- #
# Course: PYTHON 220: Advanced Programming in Python
# Script Title: Lesson 5 Assignment Testing
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-05-20, Initial release
# ---------------------------------------------------------------------------- #

import os
import logging

# FIXME: Fix module relative import
from .src import database as db

logging.basicConfig(level=logging.DEBUG)

# def test_show_available_products(_show_available_products):
#     """ available products """
#     students_response = db.show_available_products()
#     assert students_response == _show_available_products

# def test_show_rentals(_show_rentals):
#     """ rentals """
#     students_response = db.show_rentals("P000003")
#     assert students_response == _show_rentals


if __name__ == "__main__":

    cwd = os.getcwd()
    logging.debug('Current Working Directory: {}'.format(cwd))

    # nwd = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    
    nwd = os.path.dirname(os.path.abspath(__file__))

    logging.debug('New Working Directory: {}'.format(nwd))

    os.chdir(nwd)
    cwd = os.getcwd()
    logging.debug('Set Working Directory to Current Directory: {}'.format(cwd))
