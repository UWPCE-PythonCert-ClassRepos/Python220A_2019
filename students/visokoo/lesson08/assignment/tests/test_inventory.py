"""
    Autograde Lesson 8 assignment

"""

import pytest
import os
import csv
from src import inventory as l


@pytest.fixture
def _furniture_data():
    """
    underscore required on fixture to eliminate an
    invalid redefinition warning
    from pytest pylint

    """
    return [
        ("Elisa Miles", "LR04", "Leather Sofa", "25.00", "rented_items.csv"),
        ("Edward Data", "KT78", "Kitchen Table", "10.00", "rented_items.csv")
    ]


def test_add_furniture(_furniture_data):
    for row in _furniture_data:
        l.add_furniture(row[0], row[1], row[2], row[3], row[4])

    assert os.path.isfile("rented_items.csv")
    file = open("rented_items.csv", "r")
    assert file.readline() == 'Elisa Miles,LR04,Leather Sofa,25.00\n'
    assert file.readline() == 'Edward Data,KT78,Kitchen Table,10.00\n'
    file.close()
    # clean up created file

    os.unlink("rented_items.csv")


def test_single_customer():
    create_invoice = l.single_customer("Susan Wong", "rented_items_single.csv")
    create_invoice("test_items.csv")
    assert os.path.isfile("rented_items_single.csv")
    file = open("rented_items_single.csv", "r")
    assert file.readline() == 'LR04,Leather Belt,25.00\n'
    assert file.readline() == 'KT78,Cabinet Top,1000.00\n'
    os.unlink("rented_items_single.csv")


    