
""" This is an integration test module """
import pytest
import sys
import os
import peewee

# dynamically connect to the database
# as long as data, src, and tests are all located
# in the same directory.
db_folder = os.getcwd()
db_location = str(db_folder[:-6] + '\src')
input_data = str(db_folder[:-6] + '\data\customer.csv')

sys.path.append(db_location)

import basic_operations as l

@pytest.fixture
def _add_customers():
    return [
        ("123", "Name", "Lastname", "Address", "phone", "email", "Active", 999),
        ("456", "Name", "Lastname", "Address", "phone", "email", "inActive", 10),
        ("123", "Name", "Lastname", "Address", "phone", "email", "Active", 999),
        ("789", "Name", "Lastname", "Address", "phone", "email", "Active", 0),
        ("345", "Name", "Lastname", "Address", "phone", "email", "Active", -10),
        ("0123", "Name", "Lastname", "Address", "phone", "email", "Active", 999),
        ("777", "Name", "Lastname", "Address", "phone", "email", "Active", 999)
    ]

@pytest.fixture
def _search_customers():
    return [
        ("998", "Name", "Lastname", "Address", "phone", "email", "Active", 999),
         ("997", "Name", "Lastname", "Address", "phone", "email", "inActive", 10),
        ("999", "Name", "Lastname", "Address", "phone", "email", "inActive", 120)
    ]

@pytest.fixture
def _delete_customers():
    return [
        ("898", "Name", "Lastname", "Address", "phone", "email", "Active", 999),
        ("897", "Name", "Lastname", "Address", "phone", "email", "inActive", 10)
    ]

@pytest.fixture
def _list_active_customers():
    return [
        ("598", "Name", "Lastname", "Address", "phone", "email", "Active", 999),
        ("597", "Name", "Lastname", "Address", "phone", "email", "inActive", 10),
        ("596", "Name", "Lastname", "Address", "phone", "email", "inActive", 99),
        ("595", "Name", "Lastname", "Address", "phone", "email", "Active", 999),
        ("594", "Name", "Lastname", "Address", "phone", "email", "Active", 10),
        ("593", "Name", "Lastname", "Address", "phone", "email", "Active", 99)
    ]

@pytest.fixture
def _update_customer_credit():
    return [
        ("798", "Name", "Lastname", "Address", "phone", "email", "Active", 999),
        ("797", "Name", "Lastname", "Address", "phone", "email", "inActive", 10),
        ("796", "Name", "Lastname", "Address", "phone", "email", "inActive", -99)
    ]

@pytest.fixture
def _data():
    return input_data

def test_add_customer(_add_customers):
    """ additions """
    for customer in _add_customers:
        l.add_customer(customer[0],
                       customer[1],
                       customer[2],
                       customer[3],
                       customer[4],
                       customer[5],
                       customer[6],
                       customer[7]
                       )
        added = l.search_customer(customer[0])
        assert added['cust_name'] == customer[1]
        assert added['cust_last_name'] == customer[2]
        assert added['cust_email'] == customer[5]
        assert added['cust_phone'] == customer[4]

    for customer in _add_customers:
        l.delete_customer(customer[0])



def test_search_customer(_search_customers):
    """ search """
    for customer in _search_customers:
        l.add_customer(customer[0],
                       customer[1],
                       customer[2],
                       customer[3],
                       customer[4],
                       customer[5],
                       customer[6],
                       customer[7]
                       )

    result = l.search_customer(102910)
    assert result == None

    result = l.search_customer(_search_customers[2][0])
    assert result['cust_name'] == _search_customers[2][1]
    assert result['cust_last_name'] == _search_customers[2][2]
    assert result['cust_email'] == _search_customers[2][5]
    assert result['cust_phone'] == _search_customers[2][4]

    for customer in _search_customers:
        l.delete_customer(customer[0])

def test_delete_customer(_delete_customers):
    """ delete """
    for customer in _delete_customers:
        l.add_customer(customer[0],
                       customer[1],
                       customer[2],
                       customer[3],
                       customer[4],
                       customer[5],
                       customer[6],
                       customer[7]
                       )

        response = l.delete_customer(customer[0])
        assert response is True

        deleted = l.search_customer(customer[0])
        assert deleted == None

def test_update_customer_credit(_update_customer_credit):
    """ update """
    for customer in _update_customer_credit:
        l.add_customer(customer[0],
                       customer[1],
                       customer[2],
                       customer[3],
                       customer[4],
                       customer[5],
                       customer[6],
                       customer[7]
                       )

    l.update_customer_credit("798", 0)
    l.update_customer_credit("797", 1000)
    l.update_customer_credit("797", -42)
    l.update_customer_credit("796", 500)

    for customer in _update_customer_credit:
        l.delete_customer(customer[0])


def test_list_active_customers(_list_active_customers):
    """ Actives """
    for customer in _list_active_customers:
        l.add_customer(customer[0],
                       customer[1],
                       customer[2],
                       customer[3],
                       customer[4],
                       customer[5],
                       customer[6],
                       customer[7]
                       )
    actives = l.list_active_customers()

    assert actives == 4

    for customer in _list_active_customers:
        l.delete_customer(customer[0])

def test_load_csv(_data):

    test = l.load_customer_data(_data)
    ct = 0
    cust_id_list = []
    for customer in test:
        if ct < 40:
            l.add_customer(customer[0],
                           customer[1],
                           customer[2],
                           customer[3],
                           customer[4],
                           customer[5],
                           customer[6],
                           customer[7]
                           )
            cust_id_list.append(customer[0])
            ct += 1
        else:
            break

    actives = l.list_active_customers()
    assert actives == 30


    for customer in cust_id_list:
        l.delete_customer(customer)


