from unittest import TestCase
from unittest.mock import MagicMock
from unittest.mock import patch
from inventory_management import main
from inventory_class import Inventory
from furniture_class import Furniture
from electric_appliances_class import ElectricAppliances


class MainTest(unittest.TestCase):
    """Tests for main.py:
    1. does each prompt work in 'main_menu'.
    2. when adding content to 'add_new_item', item is added to the dictionary.
    3. 'item_info' either prints the dictionary or 'Item not found in Inventory' """

    def test_main(self):


class InventoryTest(unittest.TestCase):
    """Tests for inventory_class
    Not a test, but would like to think about, if any of the codes have a specific
    format, such as numbers only.
    1. can take 4 input items and create a dictionary"""

    def test_dic_values(self):
        test_dic = {'0u812': {'product_code': '0u812', 'description': 'new', 'market_price': 24, 'rental_price': '70'}}
        product_code = '0u812'
        description = 'new'
        market_price = 24
        rental_price = 70
        self.assertEqual(test_dic, output_dict)
        

class FurnitureTest(unittest.TestCase):
    """Tests for furniture_class
    1. can take 6 input items and create a dictionary"""
    pass


class ElectricAppliancesTest(unittest.TestCase):
    """Tests for electric_appliances_class
     1. can take 6 input items and create a dictionary"""
    pass


class MarketPriceTest(unittest.TestCase):
    """Test for market_prices
    1. can return a value for latest price """
    pass
