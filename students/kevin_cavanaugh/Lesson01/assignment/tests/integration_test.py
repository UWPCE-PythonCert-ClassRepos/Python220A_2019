"""
This is an integration test module for assignment
"""

from unittest import TestCase
from unittest.mock import MagicMock, patch

from inventory_management import main
from inventory_management import market_prices


class ModuleTests(TestCase):
    """
    Testing all of the classes in an integrated environment
    """
    def test_main(self):
        """
        Testing all user options together
        """
        with patch('builtins.input', lambda value: '1'):
            main.main_menu()
            market_prices.get_latest_price = MagicMock(return_value=24)

        input_info = [1, 'desk', 55, 'n', 'n']
        with patch('builtins.input', side_effect=input_info):
            new_item = main.add_new_item()
        self.assertEqual({
                'product_code': 1,
                'description': 'desk',
                'market_price': 24,
                'rental_price': 55
            }, new_item)

        input_info = [2, 'microwave', 80, 'n', 'y', 'Whirlpool', 175]
        with patch('builtins.input', lambda value: '1'):
            main.main_menu()
            market_prices.get_latest_price = MagicMock(return_value=24)
        with patch('builtins.input', side_effect=input_info):
            new_item = main.add_new_item()
        self.assertEqual({
                'product_code': 2,
                'description': 'microwave',
                'market_price': 24,
                'rental_price': 80,
                'brand': 'Whirlpool',
                'voltage': 175
            }, new_item)

        input_info = [3, 'stool', 25, 'y', 'wood', 'small']
        with patch('builtins.input', lambda value: '1'):
            main.main_menu()
            market_prices.get_latest_price = MagicMock(return_value=24)

        with patch('builtins.input', side_effect=input_info):
            new_item = main.add_new_item()
        self.assertEqual({
                'product_code': 3,
                'description': 'stool',
                'market_price': 24,
                'rental_price': 25,
                'material': 'wood',
                'size': 'small'
            }, new_item)

        with patch('builtins.input', lambda value: '2'):
            main.main_menu()

            with patch('builtins.input', lambda value: 1):
                item_dict = main.item_info()[0]
                self.assertDictEqual({
                        'product_code': 1,
                        'description': 'desk',
                        'market_price': 24,
                        'rental_price': 55
                    }, item_dict)

        with patch('builtins.input', lambda value: '2'):
            main.main_menu()

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

        with patch('builtins.input', lambda value: '2'):
            main.main_menu()

            with patch('builtins.input', lambda value: 3):
                item_dict = main.item_info()[0]
                self.assertDictEqual({
                        'product_code': 3,
                        'description': 'stool',
                        'market_price': 24,
                        'rental_price': 25,
                        'material': 'wood',
                        'size': 'small'
                    }, item_dict)

        with patch('builtins.input', lambda value: 'q'):
            main.main_menu()
            self.assertRaises(SystemExit)
