'''
# Title: test_unit.py
# Desc: Performs unittests Assignment02
# Change Log: (Who, When, What)
'''

from unittest import TestCase
from inventory_management.InventoryClass import Inventory
from inventory_management.FurnitureClass import Furniture
from inventory_management.ElectricAppliancesClass import ElectricAppliances
from inventory_management.MarketPrices import get_latest_price


class TestInventoryClass(TestCase):
    """
    Contains unit tests for Inventory.py Class

    """

    def test_initializer(self):
        """
        Tests the initializer of the Inventory class.
        Verifies classes attributes are filled when
        class is instantiated.
        :return: None

        """
        # Create an instance of the Inventory Class
        inventory = Inventory("1", "2", "3", "4")

        # Test to verify data has been passed through the
        # initializer
        self.assertIsNotNone(inventory.product_code)
        self.assertIsNotNone(inventory.description)
        self.assertIsNotNone(inventory.market_price)
        self.assertIsNotNone(inventory.rental_price)

    def test_return_as_dictionary(self):
        """
        Tests the return as dictionary method of
        the inventory class. Ensures the length
        of returned dictionary matches desired
        length.

        :return: None

        """
        # Create an instance of the Inventory Class
        inventory = Inventory("1", "2", "3", "4")
        # Obtain dictionary through return_as_dictionary
        # method for comparison
        test_dic = inventory.return_as_dictionary()

        # Verify return_as_dictionary function populates
        # Each item, and are properly instantiated
        self.assertEqual(4, len(test_dic))
        self.assertEqual('1', test_dic['product_code'])
        self.assertEqual('2', test_dic['description'])
        self.assertEqual('3', test_dic['market_price'])
        self.assertEqual('4', test_dic['rental_price'])


class TestFurnitureClass(TestCase):
    """
    Contains unit tests for Furniture.py Class

    """

    def test_initializer(self):
        """
        Tests the initializer of the Inventory class.
        Verifies classes attributes are filled when
        class is instantiated.
        :return: None

        """
        # Create an instance of the Furniture Class
        furniture = Furniture("1", "2", "3", "4", "5", "6")

        # Test to verify data has been passed through the
        # initializer
        self.assertIsNotNone(furniture.product_code)
        self.assertIsNotNone(furniture.description)
        self.assertIsNotNone(furniture.market_price)
        self.assertIsNotNone(furniture.rental_price)
        self.assertIsNotNone(furniture.material)
        self.assertIsNotNone(furniture.size)

    def test_return_as_dictionary(self):
        """
        Tests the return as dictionary method of
        the Furniture class. Ensures the length
        of returned dictionary matches desired
        length.

        :return: None

        """
        # Create an instance of the Furniture Class
        furniture = Furniture("1", "2", "3", "4", "5", "6")
        # Obtain dictionary through return_as_dictionary
        # method for comparison
        test_dic = furniture.return_as_dictionary()

        # Verify return_as_dictionary function populates
        # Each item, and are properly instantiated
        self.assertEqual(6, len(test_dic))
        self.assertEqual('1', test_dic['product_code'])
        self.assertEqual('2', test_dic['description'])
        self.assertEqual('3', test_dic['market_price'])
        self.assertEqual('4', test_dic['rental_price'])
        self.assertEqual('5', test_dic['material'])
        self.assertEqual('6', test_dic['size'])


class TestElectricAppliancesClass(TestCase):
    """
    Contains unit tests for ElectricAppliances.py Class

    """

    def test_initializer(self):
        """
        Tests the initializer of the Inventory class.
        Verifies classes attributes are filled when
        class is instantiated.
        :return: None

        """
        # Create an instance of the Electric Appliances
        electric_appliance = ElectricAppliances("1", "2", "3", "4", "5", "6")

        # Test to verify data has been passed through the
        # initializer
        self.assertIsNotNone(electric_appliance.product_code)
        self.assertIsNotNone(electric_appliance.description)
        self.assertIsNotNone(electric_appliance.market_price)
        self.assertIsNotNone(electric_appliance.rental_price)
        self.assertIsNotNone(electric_appliance.brand)
        self.assertIsNotNone(electric_appliance.voltage)

    def test_return_as_dictionary(self):
        """
        Tests the return as dictionary method of
        the electric appliance class. Ensures the length
        of returned dictionary matches desired
        length.

        :return: None

        """
        # Create an instance of the Electric Appliances Class
        electric_appliance = ElectricAppliances("1", "2", "3", "4", "5", "6")
        test_dic = electric_appliance.return_as_dictionary()

        # Verify return_as_dictionary function populates
        # Each item, and are properly instantiated
        self.assertEqual(6, len(test_dic))
        self.assertEqual('1', test_dic['product_code'])
        self.assertEqual('2', test_dic['description'])
        self.assertEqual('3', test_dic['market_price'])
        self.assertEqual('4', test_dic['rental_price'])
        self.assertEqual('5', test_dic['brand'])
        self.assertEqual('6', test_dic['voltage'])


class TestMarketPrices(TestCase):
    """
    Contains Unit tests for MarketPrices.py Class

    """

    def test_get_latest_price(self):
        """
        Tests the get_latest_price method
        of the TestMarketPrices Class.
        :return: None
        """
        # Calles the get latest price Function
        price = get_latest_price()

        # Assures the returned price is correct
        self.assertEqual(24, price)
