from unittest import TestCase
import basic_operations as bo
from peewee import *
from customer_model import *

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

        bo.add_customer('C00001', 'Kevin', 'Cavanaugh', '123 Main St',
                     '5551231234', 'email@gmail.com', 'Active', '750000')

        new_test_cust = ['C00001', 'Kevin', 'Cavanaugh', '123 Main St',
                         '5551231234', 'email@gmail.com', 'Active', '750000']

        self.assertEqual(new_test_cust[0], Customer.customer_id)
        self.assertEqual(new_test_cust[1], Customer.first_name)
        self.assertEqual(new_test_cust[2], Customer.last_name)
        self.assertEqual(new_test_cust[3], Customer.home_address)
        self.assertEqual(new_test_cust[4], Customer.phone_number)
        self.assertEqual(new_test_cust[5], Customer.email_address)
        self.assertEqual(new_test_cust[6], Customer.status)
        self.assertEqual(new_test_cust[7], Customer.credit_limit)

    def test_search_customer(self):
        bo.add_customer('C00001', 'Kevin', 'Cavanaugh', '123 Main St',
                     '5551231234', 'email@gmail.com', 'Active', '750000')

        search = bo.search_customer('C00001')

        test_search = {
            'first_name': 'Kevin',
            'last_name': 'Cavanaugh',
            'email_address': 'email@gmail.com',
            'phone_number': '5551231234'
        }

        self.assertDictEqual(test_search, search)

    def test_list_active_customers(self):
        bo.add_customer('C00001', 'Kevin', 'Cavanaugh', '123 Main St',
                     '5551231234', 'email@gmail.com', 'Active', '750000')

        self.assertEqual(1, bo.list_active_customers())

    def test_delete_customer(self):
        bo.add_customer('C00001', 'Kevin', 'Cavanaugh', '123 Main St',
                     '5551231234', 'email@gmail.com', 'Active', '750000')

        self.assertEqual(True, bo.delete_customer('C00001'))

    def test_update_customer(self):
        bo.add_customer('C00001', 'Kevin', 'Cavanaugh', '123 Main St',
                     '5551231234', 'email@gmail.com', 'Active', '750000')
        self.assertEqual(True, bo.update_customer('C00001', 1500000))


if __name__ == "__main__":
    unittest.main()
