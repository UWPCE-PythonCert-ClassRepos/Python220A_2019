# test_integration module
# tests the integration of all modules within
# inventory_management
# Russ Large, created script (4/16/2019)

from unittest import TestCase
from unittest.mock import patch
import unittest.mock
import sys

# append system path, so main can be imported as 'import main'
sys.path.append(r'C:\Python220\Lesson01\assignment\inventory_management')

import io
import main


class test_main(TestCase):
    '''This class will test the main and all functinality.'''

    def test_add_new_item(self):

        mock_input = [2, "test_description", 15, 'n', 'y', "test_brand", '34kw']

        with unittest.mock.patch('builtins.input', side_effect=mock_input):
            main.add_new_item()
            self.assertIn(2, main.full_inventory)
            new_dict = main.full_inventory[2]
            self.assertEqual("test_description", new_dict['description'])
            self.assertEqual(15, new_dict['rental_price'])
            self.assertEqual("test_brand", new_dict['brand'])
            self.assertEqual('34kw', new_dict['voltage'])

    def test_item_info(self):
        mock_input = [12, "test_description", 15, 'n', 'y', "test_brand", '34kw']

        with unittest.mock.patch('builtins.input', side_effect=mock_input):
            main.add_new_item()
            self.assertIn(12, main.full_inventory)
            new_dict = main.full_inventory[12]
            self.assertEqual("test_description", new_dict['description'])
            self.assertEqual(15, new_dict['rental_price'])
            self.assertEqual("test_brand", new_dict['brand'])
            self.assertEqual('34kw', new_dict['voltage'])

        with unittest.mock.patch('builtins.input', side_effect=mock_input):

            main.item_info()

            test2 = {'product_code': 12, 'description': 'test_description',
                    'market_price': 24, 'rental_price': 15,
                    'brand': 'test_brand', 'voltage': '34kw'}

            # See TEST_IMPROVEMENTS

    def test_exit2(self):
        with self.assertRaises(SystemExit) as cm:
            main.exit_program()
            self.assertEqual(cm.exception, "Error")

    def test_market_prices(self):
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_out:
            main.get_price()
            fake_out = fake_out.getvalue()
            fake_out = fake_out.strip()
            self.assertEqual(fake_out, "Get price")

    # def test_main_menu(self):
    #     mock_input = [2]
    #
    #     with unittest.mock.patch('builtins.input', side_effect=mock_input):
    #         main.main_menu()
    #         self.assertIn(2, main.full_inventory)
    #         new_dict = main.full_inventory[12]

    # See TEST_IMPROVEMENTS



###################
#TEST_IMPROVEMENTS#
###################

# line 34
# ---class test_main, method test_item_info---
# This part proved troubling. I wanted to take mock_input, run it through
# main.add_new_item, and then use main.item_info() to test the print output.
# Please add comments or help on this portion if possible.

# line 68
# ---class test_main, method test_main_menu---
# Testing the main_menu proved difficult as I wanted to initialize
# user_prompt, but was not sure how I could do this. Possibly stringIO method,
# but what I tried did not work properly.