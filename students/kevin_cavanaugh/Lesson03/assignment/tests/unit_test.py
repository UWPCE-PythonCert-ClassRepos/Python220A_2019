from unittest import TestCase
from src.basic_operations import *
from peewee import *

database = SqliteDatabase(':memory:')


class BasicOperationsTests(TestCase):

    def setUp(self):

        database.bind([Customer], bind_refs=False, bind_backrefs=False)
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        database.create_tables([Customer])

    def tearDown(self):

        database.drop_tables([Customer])
        database.close()

    def test_add_customer(self):

        add_customer(1, 'Kevin', 'Cavanaugh', '123 Main St',
                     5551231234, 'email@gmail.com', True, 750000)

        new_test_cust = [1, 'Kevin', 'Cavanaugh', '123 Main St',
                         5551231234, 'email@gmail.com', True, 750000]

        self.assertEqual(new_test_cust[0], Customer.customer_id)
        self.assertEqual(new_test_cust[1], Customer.first_name)
        self.assertEqual(new_test_cust[2], Customer.last_name)
        self.assertEqual(new_test_cust[3], Customer.home_address)
        self.assertEqual(new_test_cust[4], Customer.phone_number)
        self.assertEqual(new_test_cust[5], Customer.email_address)
        self.assertEqual(new_test_cust[6], Customer.status)
        self.assertEqual(new_test_cust[7], Customer.credit_limit)

    def test_search_customer(self):
        add_customer(1, 'Kevin', 'Cavanaugh', '123 Main St',
                     5551231234, 'email@gmail.com', True, 750000)
        search = search_customer(1)

        test_search = {
            'first_name': 'Kevin',
            'last_name': 'Cavanaugh',
            'email_address': 'email@gmail.com',
            'phone_number': 5551231234
        }

        self.assertEqual(test_search, search)

    def test_list_active_customers(self):
        add_customer(1, 'Kevin', 'Cavanaugh', '123 Main St',
                     5551231234, 'email@gmail.com', True, 750000)

        self.assertEqual(1, list_active_customers())

    def test_delete_customer(self):
        add_customer(1, 'Kevin', 'Cavanaugh', '123 Main St',
                     5551231234, 'email@gmail.com', True, 750000)

        self.assertEqual(True, delete_customer(1))

    def test_update_customer(self):
        add_customer(1, 'Kevin', 'Cavanaugh', '123 Main St',
                     5551231234, 'email@gmail.com', True, 750000)
        self.assertEqual(True, update_customer(1, 1500000))

if __name__ == "__main__":
    unittest.main()
