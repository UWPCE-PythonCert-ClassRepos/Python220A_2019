# ---------------------------------------------------------------------------- #
# Course: PYTHON 220: Advanced Programming in Python
# Script Title: Lesson 5 Assignment Testing
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-05-20, Initial release
# ---------------------------------------------------------------------------- #

import os
import logging
import pytest

# FIXME: Fix module relative import to test from test folder
import database as db

logging.basicConfig(level=logging.DEBUG)

@pytest.fixture
def _show_available_products():
    return [
            {'product_id': 'prd001',
             'description': '60 - inch TV stand',
             'product_type': 'livingroom',
             'quantity_available': '3'
             },
            {'product_id': 'prd002',
             'description': 'L - shaped sofa',
             'product_type': 'livingroom',
             'quantity_available': '1'
             }
            ]


@pytest.fixture
def _show_customer():
    return [
        {'user_id': 'user001', 'name': 'Elisa Miles', 'address': '4490 Union Street', 'zip_code': '98109', 'phone_number': '206-922-0882', 'email': 'elisa.miles@yahoo.com'},
        {'user_id': 'user002', 'name': 'Maya Data', 'address': '4936 Elliot Avenue', 'zip_code': '98115', 'phone_number': '206-777-1927', 'email': 'mdata@uw.edu'}
    ]


@pytest.fixture
def _show_rentals():
    return [
        {'product_id': 'prd003', 'user_id': 'user004'},
        {'product_id': 'prd002', 'user_id': 'user008'}
        ]



def test_show_available_products(_show_available_products):
    """ available products """
    students_response = db.show_available_products()
    assert students_response == _show_available_products

def test_show_rentals(_show_rentals):
    """ rentals """
    students_response = db.show_rentals("P000003")
    assert students_response == _show_rentals


def test_show_customers(_show_customer):
    pass

if __name__ == "__main__":

    cwd = os.getcwd()
    logging.debug('Current Working Directory: {}'.format(cwd))

    # nwd = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    
    nwd = os.path.dirname(os.path.abspath(__file__))

    logging.debug('New Working Directory: {}'.format(nwd))

    os.chdir(nwd)
    cwd = os.getcwd()
    logging.debug('Set Working Directory to Current Directory: {}'.format(cwd))
