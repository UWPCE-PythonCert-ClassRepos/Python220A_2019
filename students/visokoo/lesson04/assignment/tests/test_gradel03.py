"""
    Autograde Lesson 3 assignment
    Run pytest
    Run coverage and linitng using standard batch file
    Student should submit an empty database

"""

import os
import pytest

from src import basic_operations as l


@pytest.fixture
def _add_customers():
    return [
        ("123", "Name", "Lastname", "Address", "phone", "email", "active", 999),
        ("456", "Name", "Lastname", "Address", "phone", "email", "inactive", 10),
        ("123", "Name", "Lastname", "Address", "phone", "email", "active", 999),
        ("789", "Name", "Lastname", "Address", "phone", "email", "active", 0),
        ("345", "Name", "Lastname", "Address", "phone", "email", "active", -10),
        ("0123", "Name", "Lastname", "Address", "phone", "email", "active", 999),
        ("777", "Name", "Lastname", "Address", "phone", "email", "active", 999)
    ]


@pytest.fixture
def _search_customers():  # needs to del with database
    return [
        ("998", "Name", "Lastname", "Address", "phone", "email", "active", 999),
        ("997", "Name", "Lastname", "Address", "phone", "email", "inactive", 10),
        ("999", "Name", "Lastname", "Address", "phone", "email", "active", 100)
    ]


@pytest.fixture
def _delete_customers():  # needs to del with database
    return [
        ("898", "Name", "Lastname", "Address", "phone", "email", "active", 999),
        ("897", "Name", "Lastname", "Address", "phone", "email", "inactive", 10)
    ]


@pytest.fixture
def _update_customer_credit():  # needs to del with database
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


def test_delete_all_rows():
    """ Delete any existing data in the table to start fresh """
    l.LOGGER.info("Delete rows")
    l.delete_all_rows()


def test_list_active_customers(_list_active_customers):
    """ actives """
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
        assert added["name"] == customer[1]
        assert added["last_name"] == customer[2]
        assert added["email_address"] == customer[5]
        assert added["phone_number"] == customer[4]

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

    result = l.search_customer(1000)  # check nonexistent customer
    assert result == {}

    result = l.search_customer(_search_customers[1][0])
    assert result["name"] == _search_customers[1][1]
    assert result["last_name"] == _search_customers[1][2]
    assert result["email_address"] == _search_customers[1][5]
    assert result["phone_number"] == _search_customers[1][4]

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
        assert deleted == {}


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
    with pytest.raises(ValueError) as excinfo:
        l.update_customer_credit("00100", 1000)  # error
        assert 'NoCustomer' in str(excinfo.value)


@pytest.mark.datafiles(os.getcwd() + '/data')
def test_load_data(datafiles):
    """ verify that data load from file works """
    # make sure dir has at least one file
    assert len(os.listdir(datafiles)) == 1
    file = os.listdir(datafiles)[0]
    iterable = l.load_data(f"{datafiles}/{file}")
    count = 0
    while count < 10:  # take 10 values from iterator
        iter_value = next(iterable)
        l.add_customer(*iter_value)
        count += 1
    actives = l.list_active_customers()
    assert actives == 10  # check for actives
    added = l.search_customer(iter_value[0])
    assert added["name"] == iter_value[1]
    assert added["home_address"] == iter_value[3]
