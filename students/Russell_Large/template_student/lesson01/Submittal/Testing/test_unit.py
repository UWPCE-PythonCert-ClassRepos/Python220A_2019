# test_unit module
# tests indv modules within inventory_management
# Russ Large, created script (4/16/2019)

from unittest import TestCase
from unittest.mock import patch
import unittest.mock
import sys


sys.path.append(r'C:\Python220\Lesson01\assignment\inventory_management')

from furniture_class import Furniture
from electric_appliances_class import electrical_appliance
from inventory_class import Inventory
from market_prices import get_latest_price


class test_module_tests(TestCase):
    '''This class contains test methods for all modules in the inventory_management
    directory.'''

    def test_furniture_class(self):
        '''This method will initialize the __init__ in the Furniture class,
        and then test all items'''
        Furniture.product_code = 12
        Furniture.description = "test_description"
        Furniture.market_price = 24
        Furniture.rental_price = 15
        Furniture.material = 'test_material'
        Furniture.size = '50x10x2'

        true_dict = {'product_code': 12, 'description': 'test_description',
                     'market_price': 24, 'rental_price': 15,
                     'material': 'test_material', 'size': '50x10x2'}


        # Test all initializers into the Furniture class, and use
        # 'return_as_dictionary' to produce results. if the functions do
        # not work, the ValueError exception will be raised.
        try:
            test_items = Furniture(Furniture.product_code, Furniture.description,
                                   Furniture.market_price, Furniture.rental_price,
                                   Furniture.material, Furniture.size)
            dict_obj = test_items.return_as_dictionary()
        except:
            raise ValueError

        # test return value, return_as_dictionary
        self.assertEqual(dict_obj, true_dict)

        # verify the number of initializers
        real_count = 6
        key_count = 0
        for furn in dict_obj:
            key_count += 1
        self.assertEqual(real_count, key_count)

    def test_electrical_appliance(self):
        '''This method will initialize the __init__ in the Furniture class,
        and then test all items'''
        electrical_appliance.product_code = 12
        electrical_appliance.description = "test_description"
        electrical_appliance.market_price = 24
        electrical_appliance.rental_price = 15
        electrical_appliance.brand = 'test_brand'
        electrical_appliance.voltage = '34kw'

        true_dict = {'product_code': 12, 'description': 'test_description',
                     'market_price': 24, 'rental_price': 15,
                     'brand': 'test_brand', 'voltage': '34kw'}

        # Test all initializers into the Furniture class, and use
        # 'return_as_dictionary' to produce results. if the functions do
        # not work, the ValueError exception will be raised.
        try:
            test_items = electrical_appliance(electrical_appliance.product_code,
                                   electrical_appliance.description,
                                   electrical_appliance.market_price,
                                   electrical_appliance.rental_price,
                                   electrical_appliance.brand,
                                   electrical_appliance.voltage)
            dict_obj = test_items.return_as_dictionary()

        except:
            raise ValueError

        # test return value, return_as_dictionary
        self.assertEqual(dict_obj, true_dict)

        #verify results
        # print(dict_obj)

        # verify the number of objects
        real_count = 6
        key_count = 0
        for keys in dict_obj:
            key_count += 1
        self.assertEqual(real_count, key_count)

    def test_inventory_class(self):
        '''This method will initialize the __init__ in the inventory class,
        and then test all items'''

        Inventory.product_code = 12
        Inventory.description = "test_description"
        Inventory.market_price = 24
        Inventory.rental_price = 15

        true_dict = {'product_code': 12, 'description': 'test_description',
                     'market_price': 24, 'rental_price': 15}

        # Test all initializers into the Furniture class, and use
        # 'return_as_dictionary' to produce results. if the functions do
        # not work, the ValueError exception will be raised.
        try:
            test_items = Inventory(Inventory.product_code,
                                   Inventory.description,
                                   Inventory.market_price,
                                   Inventory.rental_price)

            dict_obj = test_items.return_as_dictionary()

        except:
            raise ValueError

        # test return value, return_as_dictionary
        self.assertEqual(dict_obj, true_dict)

        #verify results
        # print(dict_obj)

        # verify the number of objects
        real_count = 4
        key_count = 0
        for furn in dict_obj:
            key_count += 1
        # print(key_count)
        self.assertEqual(real_count, key_count)


    def test_price(self):

        price = get_latest_price()
        self.assertEqual(24, price)


