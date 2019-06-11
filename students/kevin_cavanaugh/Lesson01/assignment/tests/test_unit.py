"""
Test module that tests methods for assignment 1
"""

from unittest import TestCase
from unittest.mock import patch

from inventory_management.inventory_class import Inventory
from inventory_management.furniture_class import Furniture
from inventory_management.electric_appliances_class import ElectricAppliances
from inventory_management import market_prices
from inventory_management import main


class InventoryTests(TestCase):
    """
    Tests Inventory class method functionality
    """
    def test_return_as_dictionary(self):
        '''
        Test ensures a proper Inventory dict is returned
        '''
        desk = Inventory(1, 'gray stand-up', 55, 70)

        test_desk = {
            'product_code': 1,
            'description': 'gray stand-up',
            'market_price': 55,
            'rental_price': 70
        }

        for key, value in test_desk.items():
            self.assertEqual(test_desk[f'{key}'],
                             desk.return_as_dictionary()[f'{key}'])
            self.assertEqual(dict, type(desk.return_as_dictionary()))


class FurnitureTests(TestCase):
    """
    Tests Furniture class method functionality
    """

    def test_return_as_dictionary(self):
        """
        Test ensures a proper Furniture dict is returned
        """
        desk = Furniture(1, 'gray stand-up', 55, 70,
                         'wood', 'large')

        test_desk = {
            'product_code': 1,
            'description': 'gray stand-up',
            'market_price': 55,
            'rental_price': 70,
            'material': 'wood',
            'size': 'large'
        }

        for key, value in test_desk.items():
            self.assertEqual(test_desk[f'{key}'],
                             desk.return_as_dictionary()[f'{key}'])
            self.assertEqual(dict, type(desk.return_as_dictionary()))


class ElectricAppliancesTests(TestCase):
    """
    Tests ElectricAppliances class method functionality
    """
    def test_return_as_dictionary(self):
        """
         Test ensures a proper ElectricAppliances dict is returned
        """
        microwave = ElectricAppliances(2, 'black counter-top',
                                       85, 100, 'whirlpool', 185)

        test_microwave = {
            'product_code': 2,
            'description': 'black counter-top',
            'market_price': 85,
            'rental_price': 100,
            'brand': 'whirlpool',
            'voltage': 185
        }

        for key, value in test_microwave.items():
            self.assertEqual(test_microwave[f'{key}'],
                             microwave.return_as_dictionary()[f'{key}'])
            self.assertEqual(dict, type(microwave.return_as_dictionary()))


class MarketPricesTests(TestCase):
    """
    Tests MarketPrices class method functionality
    """
    def test_get_latest_price(self):
        """
        Test ensures proper Market Price is returned
        """
        latest_price = market_prices.get_latest_prices()

        self.assertEqual(24, latest_price)


class MainTests(TestCase):
    """
    Tests Main method functionality
    """
    def test_add_item(self):
        """
        Ensure add item is functioning
        """
        input_info = [1, 'desk', 80, 'n', 'n']
        with patch('builtins.input', side_effect=input_info):
            new_item = main.add_new_item()
        self.assertEqual({
            'product_code': 1,
            'description': 'desk',
            'market_price': 24,
            'rental_price': 80,
        }, new_item)

    def test_add_furniture_item(self):
        """
        Ensure add furniture is functioning
        """
        input_info = [1, 'desk', 80, 'y', 'wood', 'medium']
        with patch('builtins.input', side_effect=input_info):
            new_furniture = main.add_new_item()
        self.assertEqual({
            'product_code': 1,
            'description': 'desk',
            'market_price': 24,
            'rental_price': 80,
            'material': 'wood',
            'size': 'medium'
        }, new_furniture)

    def test_add_electric_appliance_item(self):
        """
        Ensure add electric appliance is functioning
        """
        input_info = [2, 'microwave', 80, 'n', 'y', 'Whirlpool', 175]
        with patch('builtins.input', side_effect=input_info):
            new_electric_appliance = main.add_new_item()
        self.assertEqual({
            'product_code': 2,
            'description': 'microwave',
            'market_price': 24,
            'rental_price': 80,
            'brand': 'Whirlpool',
            'voltage': 175
        }, new_electric_appliance)

    def test_get_info(self):
        """
        Ensure get info is functioning
        """
        input_info = [2, 'microwave', 80, 'n', 'y', 'Whirlpool', 175]
        with patch('builtins.input', side_effect=input_info):
            main.add_new_item()
        with patch('builtins.input', lambda value: 2):
            item_dict = main.item_info()[0]
            self.assertDictEqual({
                'product_code': 2,
                'description': 'microwave',
                'market_price': 24,
                'rental_price': 80,
                'brand': 'Whirlpool',
                'voltage': 175
                }, item_dict)
        with patch('builtins.input', lambda value: 450):
            not_found = main.item_info()
            self.assertEqual(
                "Item not found in inventory", not_found)

    def test_get_price(self):
        """
        Ensure get price is functioning
        """
        input_info = [2, 'microwave', 80, 'n', 'y', 'Whirlpool', 175]
        with patch('builtins.input', side_effect=input_info):
            main.add_new_item()
        price = main.get_price(2)
        self.assertEqual(price, 80)

    def test_main_menu_add(self):
        """
        Ensure main menu option 1 is functioning
        """
        with patch('builtins.input', lambda value: '1'):
            sel = main.main_menu()
            self.assertEqual(sel.__name__, 'add_new_item')

    def test_main_menu_get(self):
        """
        Ensure main menu option 2 is functioning
        """
        with patch('builtins.input', lambda value: '2'):
            sel = main.main_menu()
            self.assertEqual(sel.__name__, 'item_info')

    def test_main_menu_quit(self):
        """
        Ensure main menu option q is functioning
        :return:
        """
        with patch('builtins.input', lambda value: 'q'):
            main.main_menu()
        self.assertRaises(SystemExit)


if __name__ == '__main__':
    unittest.main()

