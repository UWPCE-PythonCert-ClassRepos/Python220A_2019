"""
# Title: test_database.py
# Desc: Tests Written for database.py for Lesson05
# Change Log: (Who, When, What)
# KCreek, 5/3/2019, Created Script
# KCreek, 5/9/2019, Finished Initial Script
# ----------------------------- #
"""

from unittest import TestCase
from src.database import import_data
from src.database import show_available_products
from src.database import show_rentals

class TestDatabase(TestCase):
    """
    Class tests database.py module of lesson05
    """

    def test_import_data(self):
        """
        Tests the import_data function of Database.py
        :return: None
        """

        direct = "C:\\Python220A_2019\\students\\KyleCreek\\lesson05\\assignment\\data\\"
        cust = "customers.csv"
        prod = "product.csv"
        rent = "rental.csv"

        return_tuple = import_data(direct, prod, cust, rent)
        self.assertIsInstance(return_tuple, tuple)
        self.assertEqual(len(return_tuple), 4)

    def test_show_rentals(self):
        """
        Tests the show_rentals function of Database.py
        :return: None
        """
        test = show_rentals('prd003')

        self.assertIsInstance(test, list)
        self.assertLess(0,len(test))

    def test_show_available_products(self):
        """
        Tests the shoe available products list
        of database.py
        :return: none
        """

        return_available_products = show_available_products()
        self.assertIsInstance(return_available_products, list)
        self.assertLess(0, len(return_available_products))




