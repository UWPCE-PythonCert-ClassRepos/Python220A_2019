"""
    Autograde Lesson 3 assignment
    Run pytest
    Run cobverage and linitng using standard batch file
    Student should submit an empty database

"""

import pytest

import basic_operations as b_ops


@pytest.fixture
def _add_customers():
    customer_dict = {'customer_id': '6', 'first_name': 'Katee', 'last_name': 'Jane',
                     'home_address': 'lkasdjf', 'phone_number': '9876',
                     'email_address': 'none', 'customer_status': 'A',
                     'credit_limit': '231'}
    return customer_dict



@pytest.fixture
def _search_customers(): # needs to del with database
    return [
        [("998", "Name", "Lastname", "Address", "phone", "email", "active", 999),
         ("997", "Name", "Lastname", "Address", "phone", "email", "inactive", 10)],
        ("998", "000")
    ]
@pytest.fixture
def _delete_customers(): # needs to del with database
    return [
        ("898", "Name", "Lastname", "Address", "phone", "email", "active", 999),
        ("897", "Name", "Lastname", "Address", "phone", "email", "inactive", 10)
    ]

@pytest.fixture
def _update_customer_credit(): # needs to del with database
    return [
        ("798", "Name", "Lastname", "Address", "phone", "email", "active", 999),
        ("797", "Name", "Lastname", "Address", "phone", "email", "inactive", 10),
        ("796", "Name", "Lastname", "Address", "phone", "email", "inactive", -99)
    ]

@pytest.fixture
def _list_active_customers():
    return [
        ("598", "Name", "Lastname", "Address", "phone", "email", "active", 999),
        ("597", "Name", "Lastname", "Address", "phone", "email", "inactive", 10),
        ("596", "Name", "Lastname", "Address", "phone", "email", "inactive", 99),
        ("595", "Name", "Lastname", "Address", "phone", "email", "active", 999),
        ("594", "Name", "Lastname", "Address", "phone", "email", "active", 10),
        ("593", "Name", "Lastname", "Address", "phone", "email", "active", 99)
    ]

def test_list_active_customers(_list_active_customers):
    """ actives """
    for customer in _list_active_customers:
        b_ops.add_customer(customer[0],
                           customer[1],
                           customer[2],
                           customer[3],
                           customer[4],
                           customer[5],
                           customer[6],
                           customer[7]
                           )
    actives = b_ops.list_active_customers()

    assert actives == 2

    for customer in _list_active_customers:
        b_ops.delete_customer(customer[0])
'''


def test_add_customer(_add_customers):
    """ additions
    """

    b_ops.add_customer(_add_customers)
    added = b_ops.search_customer(6)
    assert added["first_name"] == Katee
    assert added["last_name"] == Jane
    assert added["email_address"] == none
    assert added["phone_number"] == 9876
    b_ops.delete_customer(6)

'''
def test_search_customer(_search_customers):
    """ search """
    for customer in _search_customers[0]:
        b_ops.add_customer(customer[0],
                           customer[1],
                           customer[2],
                           customer[3],
                           customer[4],
                           customer[5],
                           customer[6],
                           customer[7]
                           )

    result = b_ops.search_customer(_search_customers[1][1])
    assert result == {}

    result = b_ops.search_customer(_search_customers[1][0])
    assert result["name"] == _search_customers[0][1][1]
    assert result["lastname"] == _search_customers[0][1][2]
    assert result["email"] == _search_customers[0][1][5]
    assert result["phone_number"] == _search_customers[0][1][4]

    for customer in _search_customers:
        b_ops.delete_customer(customer[0])


def test_delete_customer(_delete_customers):
    """ delete """
    for customer in _delete_customers:
        b_ops.add_customer(customer[0],
                           customer[1],
                           customer[2],
                           customer[3],
                           customer[4],
                           customer[5],
                           customer[6],
                           customer[7]
                           )

        response = b_ops.delete_customer(customer[0])
        assert response is True

        deleted = b_ops.search_customer(customer[0])
        assert deleted == {}

def test_update_customer_credit(_update_customer_credit):
    """ update """
    for customer in _update_customer_credit:
        b_ops.add_customer(customer[0],
                           customer[1],
                           customer[2],
                           customer[3],
                           customer[4],
                           customer[5],
                           customer[6],
                           customer[7]
                           )

    b_ops.update_customer_credit("798", 0)
    b_ops.update_customer_credit("797", 1000)
    b_ops.update_customer_credit("797", -42)
    b_ops.update_customer_credit("796", 500)
    with pytest.raises(ValueError) as excinfo:
        b_ops.update_customer_credit("00100", 1000) # error
        assert 'NoCustomer'  in str(excinfo.value)
'''