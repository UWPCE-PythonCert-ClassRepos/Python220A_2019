""" This is an integration test module """
import pytest
from src import basic_operations as l


@pytest.fixture
def _init_data():
    """ Base data to test with """
    return [
        ("598", "John", "Doe", "Address", "phone", "email", "active", 999),
        ("597", "Jane", "Bran", "Address", "phone", "email", "inactive", 10),
        ("596", "Carol", "Nun", "Address", "phone", "email", "inactive", 99),
        ("595", "Bal", "Car", "Address", "phone", "email", "active", 999),
        ("594", "Arya", "Stark", "Address", "phone", "email", "active", 10),
        ("593", "Sansa", "Stark", "Address", "phone", "email", "active", 99)
    ]


def test_main(_init_data):
    """
        Integration tests combining add, delete, update, and list
    """

    # Adding some data to start
    for customer in _init_data:
        l.add_customer(
            customer[0],
            customer[1],
            customer[2],
            customer[3],
            customer[4],
            customer[5],
            customer[6],
            customer[7]
        )
    assert _init_data[0][1] == l.search_customer(_init_data[0][0])['name']
    assert _init_data[1][2] == l.search_customer(_init_data[1][0])['last_name']

    # Delete a customer

    deleted = l.delete_customer(594)
    assert deleted is True

    # Search for deleted customer, verify empty dict is returned
    gone = l.search_customer(594)
    assert gone == {}

    # Test updating customer credit limit
    updated = l.update_customer_credit(593, 1500)
    assert updated == 1
    new_credit = l.search_customer(593)['credit_limit']
    assert new_credit == 1500

    # Test active customer count
    active = l.list_active_customers()
    assert active == 3
