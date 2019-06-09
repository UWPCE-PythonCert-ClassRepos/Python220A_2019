# --------------------------------------------------------------------------- #
# Course: PYTHON 220: Advanced Programming in Python
# Script Title: Lesson 10 Assignment
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-06-04, Initial release
# --------------------------------------------------------------------------- #
"""HP Norton Inventory Database Manager"""

# Note: Run with 'python src/database_01.py' from Assignment directory
# via Command Prompt
# Timing functions using time module.
# TODO: Time functions using metaprogramming

import logging as l
import csv
import pymongo
import time

from pymongo import MongoClient

l.basicConfig(level=l.DEBUG)


class MongoDBConnection:
    """MongoDB Connection"""

    def __init__(self, host='localhost', port=27017):
        l.debug('Setting up Host and Port')
        self.host = host
        self.port = port
        self.connection = None

    def __enter__(self):
        l.debug('Setting up DB Connection')
        self.connection = MongoClient(self.host, self.port)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        l.debug('Closing DB Connection')
        self.connection.close()


def logger_decorator(original_function):
    log_format = "%(asctime)s:%(lineno)-4d %(levelname)s %(message)s"

    # Write to file
    # file_name = 'test_log.log'
    # logging.basicConfig(level=logging.DEBUG, format=log_format,
    #                     filename=file_name)

    # Write to console
    logging.basicConfig(level=logging.DEBUG, format=log_format)

    def wrapper(*args):
        logging.info(
            'Ran {} with args: {}'.format(
                original_function.__name__, args))
        # logging.info(original_function(*args))
        return original_function(*args)

    return wrapper
    
def import_data(directory_name, product_file, customers_file, rental_file,
                override):
    """Import data from csv files into MongoDB collections"""
    
    start = time.time()
    
    if override:
        drop_collections()

    l.debug('Data files directory: {}'
            .format(directory_name))

    l.debug('Product Data files path: {}'
            .format(directory_name + product_file))
    l.debug('Customers Data files path: {}'
            .format(directory_name + customers_file))
    l.debug('Rentals Data files path: {}'
            .format(directory_name + rental_file))

    product_items, product_count, product_error_count = \
        import_csv(directory_name + product_file)
    l.debug('Imported {} products with {} errors'
            .format(product_count, product_error_count))

    customers_items, customers_count, customers_error_count = \
        import_csv(directory_name + customers_file)
    l.debug('Imported {} customers with {} errors'
            .format(customers_count, customers_error_count))

    rental_items, rental_count, rental_error_count = \
        import_csv(directory_name + rental_file)
    l.debug('Imported {} rentals with {} errors'
            .format(rental_count, rental_error_count))

    l.debug('Instance MDB Class for data import')
    mongo = MongoDBConnection()

    with mongo:
        l.debug('Connecting to DB for data import')
        hpn_db = mongo.connection.HPNorton

        l.debug('Creating a Products Collection')
        product = hpn_db['product']

        l.debug('Creating a Customers Collection')
        customers = hpn_db['customers']

        l.debug('Creating a Rental Collection')
        rental = hpn_db['rental']

        l.debug('Adding items to Product collection')
        product.insert_many(product_items)

        l.debug('Adding items to Customers collection')
        customers.insert_many(customers_items)

        l.debug('Adding items to Rental collection')
        rental.insert_many(rental_items)

    end = time.time()
    print(end - start)

    return (product_count, customers_count, rental_count),\
           (product_error_count, customers_error_count, rental_error_count)


def import_csv(file_path):
    """Reads csv file into a dictionary"""

    start = time.time()

    l.debug('Open csv file ({}) for reading'.format(file_path))
    # TODO: Make this read quantity_available as integer instead of string
    record_count = 0
    error_count = 0

    try:
        with open(file_path, 'r', encoding='utf-8-sig') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',')
            dict_list = []

            for line in reader:
                record_count += 1
                dict_list.append(line)

    except expression as identifier:
        error_count += 1
        l.error('Error: {}'.format(identifier))

    end = time.time()
    print(end - start)

    return dict_list, record_count, error_count


def show_available_products():
    """Lists all available products for rent (quantity_available > 0)"""
    
    start = time.time()

    l.debug('Instance MDB Class to show available Products')
    mongo = MongoDBConnection()

    with mongo:
        l.debug('Connecting to DB for reading Products')
        hpn_db = mongo.connection.HPNorton
        l.debug('Read Product collection')
        product = hpn_db['product']

        l.debug('Get Product Cursor')
        product_cursor = product.find({'quantity_available': {'$gt': '0'}},
                                      {'_id': 0,
                                       'product_id': 1,
                                       'description': 1,
                                       'product_type': 1,
                                       'quantity_available': 1
                                       }).sort('product_id', pymongo.ASCENDING)

        available_products = []
        for product in product_cursor:
            available_products.append(product)

    end = time.time()
    print(end - start)

    return available_products


def show_rentals(user_id=''):
    """Shows all rental by user_id"""
    
    start = time.time()

    l.debug('Instance MDB Class to show Rentals')
    mongo = MongoDBConnection()

    with mongo:
        l.debug('Connecting to DB for reading Rentals')
        hpn_db = mongo.connection.HPNorton

        l.debug('Read Rental collection')
        rental = hpn_db['rental']

        l.debug('Get Rental Cursor')
        rental_cursor = rental.find({'user_id': user_id},
                                    {'_id': 0,
                                     'user_id': 1,
                                     'name': 1,
                                     'address': 1,
                                     'phone_number': 1,
                                     'email': 1,
                                     'product_id': 1
                                     }).sort('product_id', pymongo.ASCENDING)

        rentals = []
        for rental in rental_cursor:
            rentals.append(rental)

    end = time.time()
    print(end - start)

    return rentals


def show_customers():
    """Shows all customers by user_id"""
    
    start = time.time()

    l.debug('Instance MDB Class to show Customers')
    mongo = MongoDBConnection()

    with mongo:
        l.debug('Connecting to DB for reading Customers')
        hpn_db = mongo.connection.HPNorton

        l.debug('Read Customers collection')
        customers = hpn_db['customers']

        l.debug('Get Customers Cursor')
        customers_cursor = customers.find({},
                                          {'_id': 0,
                                           'Id': 1,
                                           'name': 1,
                                           'Last_name': 1,
                                           'Home_address': 1,
                                           'Phone_number': 1,
                                           'Email_address': 1,
                                           'Status': 1
                                           }).sort('Id',
                                                   pymongo.ASCENDING)

        customers = []
        for customer in customers_cursor:
            customers.append(customer)

    end = time.time()
    print(end - start)

    return customers


def drop_collections():
    """Deletes existing DB colletions"""
    
    start = time.time()

    l.debug('Instance MDB Class for deletion')
    mongo = MongoDBConnection()

    with mongo:
        l.debug('Connecting to DB for deletion')
        hpn_db = mongo.connection.HPNorton

        l.debug('Deleting Product Collection')
        hpn_db['product'].drop()

        l.debug('Deleting Customers Collection')
        hpn_db['customers'].drop()

        l.debug('Deleting Rental Collection')
        hpn_db['rental'].drop()

    end = time.time()
    print(end - start)


if __name__ == "__main__":
    # START_FRESH = input("Start with empty collections? (True/False)")
    START_FRESH = True

    l.debug('Starting in Main()')
    l.debug('Call function to import csv data files into DB')
    FILE_PATH = 'data/'
    import_data(FILE_PATH, 'product.csv', 'customer.csv', 'rental.csv',
                START_FRESH)

    show_available_products()
    show_rentals('C000000')
    show_customers()
