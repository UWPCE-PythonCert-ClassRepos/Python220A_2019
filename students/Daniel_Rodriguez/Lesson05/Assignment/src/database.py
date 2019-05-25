# --------------------------------------------------------------------------- #
# Course: PYTHON 220: Advanced Programming in Python
# Script Title: Lesson 5 Assignment
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-05-20, Initial release
# --------------------------------------------------------------------------- #
# Here is what you need to do:
#  1. Create a product database with attributes that reflect the contents
#     of the csv file.
#  2. Import all data in the csv files into your MongoDB implementation.
#  3. Write queries to retrieve the product data.
#  4. Write a query to integrate customer and product data.
# --------------------------------------------------------------------------- #
"""HP Norton Inventory Database Manager"""

import logging
import csv
import os
import pymongo

from pymongo import MongoClient

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


def import_data(directory_name, product_file, customers_file, rental_file,
                override):
    """Import data from csv files into MongoDB collections"""

    if override.upper() == 'Y':
        drop_collections()

    logging.debug('Data files directory: {}'.format(directory_name))

    logging.debug('Product Data files path: {}'.format(directory_name +
                                                       product_file))
    logging.debug('Customers Data files path: {}'.format(directory_name +
                                                         customers_file))
    logging.debug('Rentals Data files path: {}'.format(directory_name +
                                                       rental_file))

    product_items, product_count, product_error_count = import_csv(directory_name +
                                                                   product_file)
    logging.debug('Imported {} products with {} errors'.format(product_count,
                                                               product_error_count))

    customers_items, customers_count, customers_error_count = import_csv(directory_name
                                                                         + customers_file)
    logging.debug('Imported {} customers with {} errors'.format(customers_count,
                                                                customers_error_count))

    rental_items, rental_count, rental_error_count = import_csv(directory_name
                                                                + rental_file)
    logging.debug('Imported {} rentals with {} errors'.format(rental_count,
                                                              rental_error_count))

    logging.debug('Instance MDB Class for data import')
    mongo = MongoDBConnection()

    with mongo:
        logging.debug('Connecting to DB for data import')
        hpn_db = mongo.connection.HPNorton

        logging.debug('Creating a Products Collection')
        product = hpn_db['product']

        logging.debug('Creating a Customers Collection')
        customers = hpn_db['customers']

        logging.debug('Creating a Rental Collection')
        rental = hpn_db['rental']

        logging.debug('Adding items to Product collection')
        product.insert_many(product_items)

        logging.debug('Adding items to Customers collection')
        customers.insert_many(customers_items)

        logging.debug('Adding items to Rental collection')
        rental.insert_many(rental_items)

    return (product_count, customers_count, rental_count),\
           (product_error_count, customers_error_count, rental_error_count)


def import_csv(file_path):
    """Reads csv file into a dictionary"""

    logging.debug('Open csv file ({}) for reading'.format(file_path))
    # TODO: Make this read quantity_available as integer instead of string
    # TODO: Remove ï»¿ character from product_id
    record_count = 0
    error_count = 0

    try:
        with open(file_path, 'r') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',')
            dict_list = []

            for line in reader:
                record_count += 1
                dict_list.append(line)

    except expression as identifier:
        error_count += 1
        logging.error('Error: {}'.format(identifier))

    return dict_list, record_count, error_count


def show_available_products():
    """Lists all available products for rent (quantity_available > 0)"""
    logging.debug('Instance MDB Class to show available Products')
    mongo = MongoDBConnection()

    with mongo:
        logging.debug('Connecting to DB for reading Products')
        hpn_db = mongo.connection.HPNorton
        logging.debug('Read Product collection')
        product = hpn_db['product']

        logging.debug('Get Product Cursor')
        product_cursor = product.find({'quantity_available': {'$gt': '0'}},
                                      {'_id': 0,
                                       'ï»¿product_id': 1,
                                       'description': 1,
                                       'product_type': 1,
                                       'quantity_available': 1}
                                      ).sort('ï»¿product_id', pymongo.ASCENDING)

        available_products = []
        for product in product_cursor:
            available_products.append(product)

    return available_products


def show_rentals(user_id=''):
    """Shows all rental by user_id"""
    logging.debug('Instance MDB Class to show Rentals')
    mongo = MongoDBConnection()

    with mongo:
        logging.debug('Connecting to DB for reading Rentals')
        hpn_db = mongo.connection.HPNorton

        logging.debug('Read Rental collection')
        rental = hpn_db['rental']

        logging.debug('Get Rental Cursor')
        rental_cursor = rental.find({'user_id': user_id},
                                    {'_id': 0,
                                     'ï»¿product_id': 1,
                                     'user_id': 1}
                                    ).sort('ï»¿product_id', pymongo.ASCENDING)

        rentals = []
        for rental in rental_cursor:
            rentals.append(rental)

    return rentals


def show_customers():
    """Shows all customers by user_id"""
    logging.debug('Instance MDB Class to show Customers')
    mongo = MongoDBConnection()

    with mongo:
        logging.debug('Connecting to DB for reading Customers')
        hpn_db = mongo.connection.HPNorton

        logging.debug('Read Customers collection')
        customers = hpn_db['customers']

        logging.debug('Get Customers Cursor')
        customers_cursor = customers.find({},
                                          {'_id': 0,
                                           'ï»¿user_id': 1,
                                           'name': 1,
                                           'address': 1,
                                           'zip_code': 1,
                                           'phone_number': 1,
                                           'e-mail': 1
                                           }).sort('ï»¿user_id',
                                                   pymongo.ASCENDING)

        customers = []
        for customer in customers_cursor:
            customers.append(customer)

    return customers


def drop_collections():
    """Deletes existing DB colletions"""
    logging.debug('Instance MDB Class for deletion')
    mongo = MongoDBConnection()

    with mongo:
        logging.debug('Connecting to DB for deletion')
        hpn_db = mongo.connection.HPNorton

        logging.debug('Deleting Product Collection')
        hpn_db['product'].drop()

        logging.debug('Deleting Customers Collection')
        hpn_db['customers'].drop()

        logging.debug('Deleting Rental Collection')
        hpn_db['rental'].drop()


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    CWD = os.getcwd()
    logging.debug('Set Working Directory to Current Directory: {}'.format(CWD))

    logging.debug('Append or Override Collections')
    # START_FRESH = input("Start with empty collections? (Y/N)")
    START_FRESH = 'Y'

    logging.debug('Starting in Main()')

    logging.debug('Call function to import csv data files into DB')
    FILE_PATH = '../data/'
    import_data(FILE_PATH, 'product.csv', 'customers.csv', 'rental.csv',
                START_FRESH)

    logging.debug('Showing available Products')
    show_available_products()

    logging.debug('Showing Rentals')
    show_rentals('user002')

    logging.debug("Showing all Customers:")
    show_customers()
