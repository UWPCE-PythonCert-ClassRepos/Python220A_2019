# --------------------------------------------------------------------------- #
# Course: PYTHON 220: Advanced Programming in Python
# Script Title: Lesson 10 Assignment
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-06-04, Initial release
# --------------------------------------------------------------------------- #
"""HP Norton Inventory Database Manager"""
# Using hard coded data to test DB functionality

from pymongo import MongoClient
from pprint import pprint
from bson import ObjectId
import logging

logging.basicConfig(level=logging.DEBUG)


class MongoDBConnection:
    """MongoDB Connection"""

    def __init__(self, host='localhost', port=27017):
        logging.debug('Setting up Host and Port')
        self.host = host
        self.port = port
        self.connection = None

    def __enter__(self):
        logging.debug('Setting up DB Connection')
        self.connection = MongoClient(self.host, self.port)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        logging.debug('Closing DB Connection')
        self.connection.close()


def print_mdb_collection(collection_name):
    logging.debug('Printing all Collection Data')
    for doc in collection_name.find():
        pprint(doc)


def import_data(directory_name, products_file, customer_file, rentals_file):
    logging.debug('Instance MDB Class for data import')
    mongo = MongoDBConnection()

    with mongo:
        logging.debug('Connecting to DB for data import')
        db = mongo.connection.HPNorton

        logging.debug('Creating a Products Collection')
        product = db['product']

        logging.debug('Creating a Customers Collection')
        customers = db['customers']

        logging.debug('Creating a Rental Collection')
        rental = db['rental']

        logging.debug('Adding items to Product collection')
        product.insert_many(products_file)

        logging.debug('Adding items to Customers collection')
        customers.insert_many(customer_file)

        logging.debug('Adding items to Rental collection')
        rental.insert_many(rentals_file)


def show_available_products():
    pass


def show_rentals():
    pass


def drop_collections():
    logging.debug('Instance MDB Class for deletion')
    mongo = MongoDBConnection()

    with mongo:
        logging.debug('Connecting to DB for deletion')
        db = mongo.connection.HPNorton

        logging.debug('Deleting Product Collection so data is not duplicated')
        db['product'].drop()

        logging.debug('Deleting Customers Collection so data is not duplicated')
        db['customers'].drop()

        logging.debug('Deleting Rental Collection so data is not duplicated')
        db['rental'].drop()


def main():

    product_items = [
            {'product_id': 'prd001',
             'description': '60 - inch TV stand',
             'product_type': 'livingroom',
             'quantity_available': 3
             },
            {'product_id': 'prd002',
             'description': 'L - shaped sofa',
             'product_type': 'livingroom',
             'quantity_available': 10
             }
            ]

    customers_items = [
        {'user_id': 'user001', 'name': 'Elisa Miles', 'address': '4490 Union Street', 'zip_code': '98109', 'phone_number': '206-922-0882', 'email': 'elisa.miles@yahoo.com'},
        {'user_id': 'user002', 'name': 'Maya Data', 'address': '4936 Elliot Avenue', 'zip_code': '98115', 'phone_number': '206-777-1927', 'email': 'mdata@uw.edu'}
    ]

    rental_items = [
        {'product_id': 'prd003', 'user_id': 'user004'},
        {'product_id': 'prd002', 'user_id': 'user008'}
        ]

    import_data('Data', product_items, customers_items, rental_items)


if __name__ == "__main__":

    logging.debug('Append or Override Collections')
    # start_fresh = input("Start with empty collections? (Y/N)")
    start_fresh = True
    if start_fresh:
        drop_collections()

    logging.debug('Starting in Main()')
    main()
