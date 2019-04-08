""" This is an integration test module """

from unittest import TestCase
from unittest.mock import MagicMock, patch

import market_prices as market_price
import main


class ModuleTests(TestCase):
    """ Combining all the classes and testing collectively """

    def test_main(self):
        """ Testing item creation with all classes and viewing the contents """
        with patch('builtins.input', lambda value: '1'):
            main.main_menu()
            market_price.get_latest_price = MagicMock(return_value=300)

        input_info = [10, 'Bar Stool', '20', 'y', 'Wood', 'S']
        with patch('builtins.input', side_effect=input_info):
            new_item = main.add_new_item()
        self.assertEqual(
            {
                'product_code': 10,
                'description': 'Bar Stool',
                'market_price': 300,
                'rental_price': '20',
                'material': 'Wood',
                'size': 'S'
            },
            new_item)

        input_info = [11, 'Dishwasher', '60', 'n', 'y', 'GE', '110']
        with patch('builtins.input', lambda value: '1'):
            main.main_menu()
            market_price.get_latest_price = MagicMock(return_value=1500)
        with patch('builtins.input', side_effect=input_info):
            new_item = main.add_new_item()
        self.assertEqual(
            {
                'product_code': 11,
                'description': 'Dishwasher',
                'market_price': 1500,
                'rental_price': '60',
                'brand': 'GE',
                'voltage': '110'
            },
            new_item)

        with patch('builtins.input', lambda value: '1'):
            main.main_menu()
            market_price.get_latest_price = MagicMock(return_value=10)

        input_info = [12, 'Toy', '5', 'n', 'n']
        with patch('builtins.input', side_effect=input_info):
            new_item = main.add_new_item()
        self.assertEqual(
            {
                'product_code': 12,
                'description': 'Toy',
                'market_price': 10,
                'rental_price': '5'
            },
            new_item)

        with patch('builtins.input', lambda value: '2'):
            main.main_menu()

            with patch('builtins.input', lambda value: 10):
                item_dict = main.item_info()[0]
                self.assertDictEqual(
                    {
                        'product_code': 10,
                        'description': 'Bar Stool',
                        'market_price': 300,
                        'rental_price': '20',
                        'material': 'Wood',
                        'size': 'S'
                    },
                    item_dict)

        with patch('builtins.input', lambda value: '2'):
            main.main_menu()

            with patch('builtins.input', lambda value: 11):
                item_dict = main.item_info()[0]
                self.assertDictEqual(
                    {
                        'product_code': 11,
                        'description': 'Dishwasher',
                        'market_price': 1500,
                        'rental_price': '60',
                        'brand': 'GE',
                        'voltage': '110'
                    },
                    item_dict)

        with patch('builtins.input', lambda value: '2'):
            main.main_menu()

            with patch('builtins.input', lambda value: 12):
                item_dict = main.item_info()[0]
                self.assertDictEqual(
                    {
                        'product_code': 12,
                        'description': 'Toy',
                        'market_price': 10,
                        'rental_price': '5'
                    },
                    item_dict)
