# ---------------------------------------------------------------------------- #
# Course: PYTHON 220: Advanced Programming in Python
# Script Title: Inventory Management Unit Testing
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-04-14, Initial release
# ---------------------------------------------------------------------------- #
"""
Unit Testing for Inventory Management
"""

from unittest import TestCase


from ..inventory_management.inventory_class import Inventory as IC
from ..inventory_management.furniture_class import Furniture as FC
from ..inventory_management.electric_appliances_class \
    import ElectricAppliances as EAC
# from .inventory_management import Market_prices as MP

# import inventory_class as IC
# import furniture_class as FC
# import electric_appliances_class as EAC


class InventoryTests(TestCase):
    """
    InventoryTests
    """
    def test_inventory_class(self):
        """
        Test class
        :return:
        """
        product = IC.Inventory('1', 'Dinner Table', '399', '29')
        self.assertEqual(product.product_code, '1')
        self.assertEqual(product.description, 'Dinner Table')
        self.assertEqual(product.market_price, '399')
        self.assertEqual(product.rental_price, '29')

        self.assertEqual(IC.Inventory.return_as_dictionary(product),
                         {'product_code': '1',
                          'description': 'Dinner Table',
                          'market_price': '399',
                          'rental_price': '29'
                          })


class ElectricAppliancesTests(TestCase):
    """
    ElectricAppliancesTests
    """
    def test_electric_appliances_class(self):
        """
        Test class
        :return:
        """
        product = EAC.ElectricAppliances('1', 'Refrigerator', '399', '29',
                                         'Samsung', '110')
        self.assertEqual(product.product_code, '1')
        self.assertEqual(product.description, 'Refrigerator')
        self.assertEqual(product.market_price, '399')
        self.assertEqual(product.rental_price, '29')
        self.assertEqual(product.brand, 'Samsung')
        self.assertEqual(product.voltage, '110')

        self.assertEqual(EAC.ElectricAppliances.return_as_dictionary(product),
                         {'product_code': '1',
                          'description': 'Refrigerator',
                          'market_price': '399',
                          'rental_price': '29',
                          'brand': 'Samsung',
                          'voltage': '110'
                          })


class FurnitureTests(TestCase):
    """
    FurnitureTests
    """
    def test_furniture_class(self):
        """
        Test class
        :return:
        """
        product = FC.Furniture('1', 'Sofa', '399', '29',
                               'Leather', 'L')
        self.assertEqual(product.product_code, '1')
        self.assertEqual(product.description, 'Sofa')
        self.assertEqual(product.market_price, '399')
        self.assertEqual(product.rental_price, '29')
        self.assertEqual(product.material, 'Leather')
        self.assertEqual(product.size, 'L')

        self.assertEqual(FC.Furniture.return_as_dictionary(product),
                         {'product_code': '1',
                          'description': 'Sofa',
                          'market_price': '399',
                          'rental_price': '29',
                          'material': 'Leather',
                          'size': 'L'
                          })


# class MainTests(TestCase):
#     def test_main_menu(self):
#         self.assertEqual(main.main_menu('q'), "Quitter!")
#
#         # with mock.patch('builtins.input', return_value="q"):
#         #     self.assertEqual(main.main_menu('q'), "Quitter!")
#
#     def test_add_new_item(self):
#         pass
#
#     def test_item_info(self):
#         pass
#
#     def test_exit_program(self):
#         pass


# class MarketPricesTest(TestCase):
#     def test_get_market_prices(self):
#         self.assertEqual(MP.get_latest_price("1"), 24)
        # = MagicMock(return_value=24)


# if __name__ == '__main__' and __package__ is None:
#     from os import sys, path
#     sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
