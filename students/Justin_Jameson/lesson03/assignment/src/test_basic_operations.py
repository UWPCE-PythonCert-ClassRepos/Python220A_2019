# -------------------------------------------------#
# # Title: Lesson 03 Test Harness
# # Dev:   Justin Jameson
# # Date:  4/20/2019
# # ChangeLog: (Who, when, What)
# -------------------------------------------------#
"""
Following guidlines set forth in: Testing Python APPLYING UNIT TESTING, TDD, BDD, AND ACCEPTANCE TESTING
- Unit tests should be placed under a test/unit directory at the top level of your project folder.
- All folders within the application's code should be mirrored by test folders under test/unit,
which will have the unit tests for each file in them.
For example, app/data should have a mirrored folder of test/unit/app/data.
- All unit test files should mirror the name of the file they are testing, with _testas the suffix.
For example, app/data/data_interface.py should have a test file of test/unit/app/data/data_interface_test.py.
"""

import pytest
import basic_operations as b_ops


@pytest.fixture
def _add_customers():
    """
    possible refactor could be defining the dict as a constant then calling each key in the specific method.
    see chapter 2 from above book:
    """

    customer_dict = {'customer_id': '6', 'first_name': 'Katee', 'last_name': 'Jane',
                     'home_address': 'Pac NW', 'phone_number': '764 206 3800',
                     'email_address': 'none', 'customer_status': 'A',
                     'credit_limit': '231'}
    return customer_dict


@pytest.fixture
def _search_customers():
    customer_id = 6
    return customer_id


@pytest.fixture
def _delete_customers():
    customer_id = 6
    return customer_id


@pytest.fixture
def _update_customer_credit():
    new_credit = 369
    customer_id = 6
    return new_credit, customer_id


@pytest.fixture
def _list_active_customers():
    return []


def test_list_active_customers(_list_active_customers):
    """ actives """

    actives = b_ops.list_active_customers()
    assert actives != 2


def test_add_customer(_add_customers):
    """ additions
    """
    # b_ops.main_menu("q")
    b_ops.add_customer(_add_customers)
    added = b_ops.search_customer(6)
    assert added["first_name"] == 'Katee'
    assert added["last_name"] == 'Jane'
    assert added["email_address"] == 'none'
    assert added["phone_number"] == '764 206 3800'
    #  b_ops.delete_customer(6)


def test_search_customer(_search_customers):
    """ search """
    # result = b_ops.search_customer(_search_customers)
    # assert result == {}, {'customer_id': '6', 'first_name': 'Katee', 'last_name': 'Jane',
    #                       'home_address': 'Pac NW', 'phone_number': '764 206 3800',
    #                       'email_address': 'none', 'customer_status': 'A',
    #                       'credit_limit': '231'}

    result = b_ops.search_customer(_search_customers)
    assert result['first_name'] == 'Katee'
    assert result["last_name"] == 'Jane'


def test_update_customer_credit(_update_customer_credit):
    """ update """
    new_credit = 369
    customer_id = 6
    b_ops.update_customer_credit(new_credit, customer_id)
    result = b_ops.search_customer(6)
    assert result['credit_limit'] == 369


def test_delete_customer(_delete_customers):
    """ delete """

    response = b_ops.delete_customer(_delete_customers)
    assert response is None

    deleted = b_ops.search_customer(_delete_customers)
    assert deleted == {}
