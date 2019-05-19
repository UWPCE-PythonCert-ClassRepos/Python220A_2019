"""
grade lesson 5
"""

import pytest

from src import database as l


@pytest.fixture
def _show_available_products():
    """ fixture for mock available products data """
    return {
        'prd001': {'description': '60-inch TV stand',
                   'product_type': 'livingroom',
                   'quantity_available': 3},
        'prd003': {'description': 'Acacia kitchen table',
                   'product_type': 'kitchen',
                   'quantity_available': 7},
        'prd004': {'description': 'Queen bed',
                   'product_type': 'bedroom',
                   'quantity_available': 10},
        'prd005': {'description': 'Reading lamp',
                   'product_type': 'bedroom',
                   'quantity_available': 20},
        'prd006': {'description': 'Portable heater',
                   'product_type': 'bathroom',
                   'quantity_available': 14},
        'prd008': {'description': 'Smart microwave',
                   'product_type': 'kitchen',
                   'quantity_available': 30},
        'prd010': {'description': '60-inch TV',
                   'product_type': 'livingroom',
                   'quantity_available': 3}
    }

@pytest.fixture
def _show_rentals():
    """ fixture for mock rentals deta """
    return {
        'C001': {'rental': [{'_id': 'user008',
                             'address': '4329 Honeysuckle Lane',
                             'email': 'harrisfamily@gmail.com',
                             'name': 'Shirlene Harris',
                             'phone_number': '206-279-5340',
                             'zip_code': 98055}],
                 'user_id': 'user008'},
        'C002': {'rental': [{'_id': 'user005',
                             'address': '861 Honeysuckle Lane',
                             'email': 'soundersoccer@mls.com',
                             'name': 'Dan Sounders',
                             'phone_number': '206-279-1723',
                             'zip_code': 98244}],
                 'user_id': 'user005'}
    }


def test_import_data():
    """ import """
    l.drop_cols("products", "customers", "rentals")
    added, errors = l.import_data(
        'data', "product.csv", "customers.csv", "rental.csv")
    for add in added:
        assert isinstance(add, int)

    for error in errors:
        assert isinstance(error, int)


def test_show_available_products(_show_available_products):
    """ available products """
    students_response = l.show_available_products()
    assert students_response == _show_available_products


def test_show_rentals(_show_rentals):
    """ rentals """
    students_response = l.show_rentals("prd002")
    assert students_response == _show_rentals