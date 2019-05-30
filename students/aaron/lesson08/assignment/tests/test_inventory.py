"""
    Autograde Lesson 8 assignment

"""

import pytest
import os

import src.inventory as i


FILENAME = 'test_data_file.csv'

@pytest.fixture
def _complete_furniture_file():
    return "customer_name,item_code,item_description,item_monthly_price\nStan Lee,DSK01,Office Desk,10.01\nStan Lee,LMP52,Desk Lamp,1.61\nStan Lee,CHR19,Office Chair,5.22\n"

@pytest.fixture
def _short_furniture_file():
    return "customer_name,item_code,item_description,item_monthly_price\nAbe Lincoln,LOG24,Fireplace Log,1.11\n"

@pytest.fixture(autouse=True)
def cleanup_after_test():
    ''' cleans up the file after every test '''
    yield
    os.remove(FILENAME)

def test_add_furniture_new_file(_short_furniture_file):
    ''' Tests output file after an add_furniture call '''
    assert os.path.isfile(FILENAME) == False
    i.add_furniture(FILENAME, 'Abe Lincoln', 'LOG24', 'Fireplace Log', 1.11)
    f = open(FILENAME, 'r')
    contents = f.read()
    f.close()
    assert contents == _short_furniture_file

def test_single_customer(_complete_furniture_file):
    ''' Tests output file after an add_furniture call '''
    items = [
        {'item_code': 'DSK01', 'item_description': 'Office Desk', 'item_monthly_price': 10.01},
        {'item_code': 'LMP52', 'item_description': 'Desk Lamp', 'item_monthly_price': 1.61},
        {'item_code': 'CHR19', 'item_description': 'Office Chair', 'item_monthly_price': 5.22}
    ]
    adder = i.single_customer('Stan Lee', FILENAME)
    adder(items)
    f = open(FILENAME, 'r')
    contents = f.read()
    f.close()
    assert contents == _complete_furniture_file
