# --------------------------------------------------------------------------- #
# Course: PYTHON 220: Advanced Programming in Python
# Script Title: Lesson 9 Assignment - Test
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-06-02, Initial release
# --------------------------------------------------------------------------- #


import pytest
import src.database as db


@pytest.fixture
def _show_available_products():
    return [
            {'product_id': 'prd001', 'description': '60-inch TV stand', 'product_type': 'livingroom', 'quantity_available': '3'},
            {'product_id': 'prd003', 'description': 'Acacia kitchen table', 'product_type': 'kitchen', 'quantity_available': '7'},
            {'product_id': 'prd004', 'description': 'Queen bed', 'product_type': 'bedroom', 'quantity_available': '10'}, 
            {'product_id': 'prd005', 'description': 'Reading lamp', 'product_type': 'bedroom', 'quantity_available': '20'}, 
            {'product_id': 'prd006', 'description': 'Portable heater', 'product_type': 'bathroom', 'quantity_available': '14'}, 
            {'product_id': 'prd008', 'description': 'Smart microwave', 'product_type': 'kitchen', 'quantity_available': '30'}, 
            {'product_id': 'prd010', 'description': '60-inch TV', 'product_type': 'livingroom', 'quantity_available': '3'}
            ]


@pytest.fixture
def _show_rentals():
    return [
            {'product_id': 'prd007', 'user_id': 'user002'},
            {'product_id': 'prd010', 'user_id': 'user002'}
            ]


@pytest.fixture
def _show_customers():
    return [
            {'user_id': 'user001', 'name': 'Elisa Miles', 'address': '4490 Union Street', 'zip_code': '98109', 'phone_number': '206-922-0882'},
            {'user_id': 'user002', 'name': 'Maya Data', 'address': '4936 Elliot Avenue', 'zip_code': '98115', 'phone_number': '206-777-1927'},
            {'user_id': 'user003', 'name': 'Andy Norris', 'address': '348 Terra Street', 'zip_code': '98501', 'phone_number': '206-309-2533'},
            {'user_id': 'user004', 'name': 'Flor Matatena', 'address': '885 Boone Crockett Lane', 'zip_code': '97209', 'phone_number': '206-414-2629'},
            {'user_id': 'user005', 'name': 'Dan Sounders', 'address': '861 Honeysuckle Lane', 'zip_code': '98244', 'phone_number': '206-279-1723'},
            {'user_id': 'user006', 'name': 'Leo Dembele', 'address': '2725 Mutton Town Road', 'zip_code': '98368', 'phone_number': '206-203-1294'},
            {'user_id': 'user007', 'name': 'Pete Nicholas', 'address': '668 Elliot Avenue', 'zip_code': '98115', 'phone_number': '206-279-8759'},
            {'user_id': 'user008', 'name': 'Shirlene Harris', 'address': '4329 Honeysuckle Lane', 'zip_code': '98055', 'phone_number': '206-279-5340'},
            {'user_id': 'user009', 'name': 'Nick Rather', 'address': '4679 Goodwin Avenue', 'zip_code': '98619', 'phone_number': '206-777-1965'},
            {'user_id': 'user010', 'name': 'Jose Garza', 'address': '2717 Raccoon Run', 'zip_code': '98116', 'phone_number': '206-946-8200'}
            ]


def test_import_data():
    """ import """

    file_path = 'data/'
    added, errors = db.import_data(file_path, "product.csv", "customers.csv", "rental.csv", 'Y')

    for add in added:
        assert isinstance(add, int)

    for error in errors:
        assert isinstance(error, int)

    assert added == (10, 10, 9)
    assert errors == (0, 0, 0)


def test_show_available_products(_show_available_products):
    """ available products """
    students_response = db.show_available_products()

    assert students_response == _show_available_products


def test_show_rentals(_show_rentals):
    """ rentals """
    students_response = db.show_rentals('user002')
    assert students_response == _show_rentals


def test_show_customers(_show_customers):
    """ rentals """
    students_response = db.show_customers()
    assert students_response == _show_customers


# if __name__ == "__main__":
#     print(sys.path)
