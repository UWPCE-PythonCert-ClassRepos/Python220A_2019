"""
# Title: test_basic_operations.py
# Desc: Tests the Basic operations of basic_operations.py
# Change Log: (Who, When, What)
# KCreek, 4/24/2019, Created Script
# KCreek, 4/27/2019, Added Test Operations
"""

from unittest import TestCase
from basic_operations import add_customer
from basic_operations import search_customer
from basic_operations import update_customer_credit
from basic_operations import delete_customer
from basic_operations import list_active_customers
import random
import logging


class TestBasicOperations(TestCase):

    """
    Tests basic_operations.py
    """

    def test_add_customer(self):
        """
        Tests the add customer functionality of basic_operations.py
        :return: None
        """
        # Create 4 Fake Customer Profiles to add to customers table in customers.db
        customer1 = [1, 'Kyle', 'Creek', '11550 6th Pl NE', '253-315-3049', 'kyle.a.creek@gmail.com', 'active', 750]
        customer2 = [2, 'Lebron', 'James', 'Somwhere in LA', '480-980-5555', 'lebron.james@yahoo.com', 'active', 1000]
        customer3 = [3, 'Lou', 'Williams', 'LA', '555-555-5555', 'lou.will.thrill@gmail.com', 'inactive', 1000]
        customer4 = [4, 'Fake', 'Kyle', 'Nigeria', '123-456-7890', 'noidea@aol.com', 'active', 100]

        cust_list = [customer1, customer2, customer3, customer4]

        # Add Initial Customers to the database
        for name_list in cust_list:
            add_customer(*name_list)

        # Check to Ensure the customers were properly added
        for customer in cust_list:
            return_dict = search_customer(customer[0])
            self.assertEqual(str(customer[0]), return_dict['customer_id'])
            self.assertEqual(str(customer[1]), return_dict['first_name'])
            self.assertEqual(str(customer[2]), return_dict['last_name'])
            self.assertEqual(str(customer[5]), return_dict['email_address'])
            self.assertEqual(str(customer[4]), return_dict['phone_number'])

        # Verify errors are raised when attempting to add existing customer ID.

    def test_search_customer(self):
        """
        Tests the search customer functionality of basic_operations.py
        :return: None
        """

        # Store list of Customer IDs
        cust_id_list = ['1', '2', '3', '4']

        # Test each customer ID to ensure queries match
        for cust_id in cust_id_list:
            return_dict = search_customer(cust_id)
            # Verify Return Data Type
            self.assertIsInstance(return_dict, dict)
            # Verify Correct IDs in place
            self.assertEqual(cust_id, return_dict['customer_id'])
            # Assert Correct Length of Dictionary
            self.assertEqual(len(return_dict), 6)

    def test_update_customer_credit(self):
        """
        Tests the Update Customer functionality of basic_operations.py
        :return: None
        """
        # Create Some integer to assign new credit limit
        new_credit_limit = random.randint(1,1000)

        # Return the initial query information
        return_dict = search_customer(1)
        old_credit = return_dict["credit_limit"]
        logging.info("Old Credit Limit {}".format(old_credit))

        # Update the Customer's Credit Limit
        update_customer_credit(1, new_credit_limit)

        # Return second Query Information
        return_dict_2 = search_customer(1)
        new_credit = return_dict_2["credit_limit"]
        logging.info("New Credit Limit {}".format(new_credit))

        self.assertNotEqual(old_credit, new_credit)

    def test_list_active_customers(self):
        """
        Tests the list active customers functionality of basic_operations.py
        :return: None
        """

        return_active = list_active_customers()
        self.assertEqual(3, return_active)

    def test_delete_customers(self):
        """
        Tests the delete customer functionality of basic_operations.py
        :return: none
        """

        # Prove Customer 1 exists
        return_dict = search_customer(1)
        self.assertIsNotNone(return_dict)

        # Delete Customer 1
        delete_customer(1)
        return_dict2 = search_customer(1)
        self.assertEqual(0, len(return_dict2))

