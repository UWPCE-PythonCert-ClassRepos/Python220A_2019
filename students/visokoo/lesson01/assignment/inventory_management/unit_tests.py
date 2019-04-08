"""
This test module tests methods in the InventoryTests class
"""
from unittest import TestCase
from unittest.mock import MagicMock, patch

from InventoryClass import Inventory
from ElectricAppliancesClass import ElectricAppliances
from FurnitureClass import Furniture
import main
import market_prices as market_price


class InventoryTests(TestCase):
    """
    InventoryTests class to test method functionality
    """
    def test_init(self):
        """
        Test that a proper Inventory object is returned
        """
        item = Inventory(1, "Item1", "200", "400")
        self.assertEqual(1, item.product_code)
        self.assertEqual("Item1", item.description)
        self.assertEqual("200", item.market_price)
        self.assertEqual("400", item.rental_price)

    def test_dict(self):
        """
        Test that a proper Inventory dict is returned
        """
        item = Inventory(1, "Item1", "200", "400")

        output_dict = item.return_as_dictionary()
        self.assertEqual(
            {
                'product_code': 1,
                'description': 'Item1',
                'market_price': '200',
                'rental_price': '400'
            },
            output_dict)


class ElectricAppliancesTests(TestCase):
    """
    ElectricAppliancesTests class to test method functionality
    """
    def test_init(self):
        """
        Test that a proper ElectricAppliances object is returned
        """
        item = ElectricAppliances(
            1,
            "EA1",
            "1000",
            "2000",
            brand="GE",
            voltage="220")
        self.assertEqual("220", item.voltage)
        self.assertEqual("GE", item.brand)
        self.assertEqual("EA1", item.description)

    def test_dict(self):
        """
        Test that a proper ElectricAppliances dict is returned
        """
        item = ElectricAppliances(
            1,
            "EA1",
            "1000",
            "2000",
            brand="GE",
            voltage="220")

        output_dict = item.return_as_dictionary()
        self.assertEqual(
            {
                'product_code': 1,
                'description': 'EA1',
                'market_price': '1000',
                'rental_price': '2000',
                'brand': 'GE',
                'voltage': '220'
            },
            output_dict)


class FurnitureTests(TestCase):
    """
    FurnitureTests class to test method functionality
    """
    def test_init(self):
        """
        Test that a proper Furniture object is returned
        """
        item = Furniture(
            1,
            "F1",
            "5000",
            "6000",
            material="Leather",
            size="L")
        self.assertEqual("Leather", item.material)
        self.assertEqual("L", item.size)
        self.assertEqual("F1", item.description)

    def test_dict(self):
        """
        Test that a proper Furniture dict is returned
        """
        item = Furniture(
            1,
            "F1",
            "5000",
            "6000",
            material="Leather",
            size="L")

        output_dict = item.return_as_dictionary()
        self.assertEqual(
            {
                'product_code': 1,
                'description': 'F1',
                'market_price': '5000',
                'rental_price': '6000',
                'material': 'Leather',
                'size': 'L'
            },
            output_dict)


class MainTests(TestCase):
    """
    MainTests class to test method functionality
    """
    def test_add_item_reg(self):
        """ Test add item """
        input_info = [3, 'Toy', '20', 'n', 'n']
        with patch('builtins.input', side_effect=input_info):
            new_item = main.add_new_item()
        self.assertEqual(
            {
                'product_code': 3,
                'description': 'Toy',
                'market_price': 24,
                'rental_price': '20'
            },
            new_item)

    def test_add_item_furniture(self):
        """ Test add furniture item """
        input_info = [2, 'Couch', '20', 'y', 'Leather', 'M']
        with patch('builtins.input', side_effect=input_info):
            new_item = main.add_new_item()
        self.assertEqual(
            {
                'product_code': 2,
                'description': 'Couch',
                'market_price': 24,
                'rental_price': '20',
                'material': 'Leather',
                'size': 'M'
            },
            new_item)

    def test_get_info(self):
        """ Test getting item info """
        input_info = [1, 'Dryer', '500', 'n', 'y', 'GE', '220']
        with patch('builtins.input', side_effect=input_info):
            main.add_new_item()
        with patch('builtins.input', lambda value: 1):
            item_dict = main.item_info()[0]
            self.assertDictEqual(
                {
                    'product_code': 1,
                    'description': 'Dryer',
                    'market_price': 24,
                    'rental_price': '500',
                    'brand': 'GE',
                    'voltage': '220'
                },
                item_dict)
        with patch('builtins.input', lambda value: 0):
            not_found = main.item_info()
            self.assertEqual(
                "Item not found in inventory", not_found)

    def test_exit(self):
        """ Test function exit """
        with self.assertRaises(SystemExit):
            main.exit_program()

    def test_main_menu_add(self):
        """ Check that selection 1 matches add_new_item function call """
        with patch('builtins.input', lambda value: '1'):
            sel = main.main_menu()
            self.assertEqual(sel.__name__, 'add_new_item')

    def test_main_menu_get(self):
        """ Check that selection 2 matches item_info function call """
        with patch('builtins.input', lambda value: '2'):
            sel = main.main_menu()
            self.assertEqual(sel.__name__, 'item_info')

    def test_main_menu_quit(self):
        """ Check that selection q matches quit function call """
        with patch('builtins.input', lambda value: 'q'):
            main.main_menu()
        self.assertRaises(SystemExit)

    def test_get_price(self):
        """ Test get_price function """
        input_info = [4, 'Stove', '1000', 'n', 'y', 'GE', '220']
        with patch('builtins.input', side_effect=input_info):
            main.add_new_item()
        price = main.get_price(4)
        self.assertEqual(price, '1000')

    def test_get_latest_price(self):
        """ Test latest market price with mock """
        market_price.get_latest_price = MagicMock(return_value=4000)
        price = market_price.get_latest_price(4)
        market_price.get_latest_price.assert_called_with(4)
        self.assertEqual(price, 4000)


# if __name__ == '__main__' and __package__ is None:
#     from os import sys, path
#     sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
