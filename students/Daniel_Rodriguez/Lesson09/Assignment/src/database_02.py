# --------------------------------------------------------------------------- #
# Course: PYTHON 220: Advanced Programming in Python
# Script Title: Lesson 9 Assignment
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-06-02, Initial release
# --------------------------------------------------------------------------- #
"""HP Norton Inventory Database Manager"""

# Note: Run with 'python src/database_02.py' from Assignment directory
# via Command Prompt


import logging
import csv
import pymongo
from pymongo import MongoClient


# Context Manager for MongoDB
class MongoDBConnection:
    """MongoDB Connection"""

    def __init__(self, host='localhost', port=27017):
        self.host = host
        self.port = port
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient(self.host, self.port)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
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


@logger_decorator
def import_data(directory_name, product_file, customers_file, rental_file,
                override):
    """Import data from csv files into MongoDB collections"""

    if override:
        drop_collections()

    product_items, product_count, product_error_count = \
        import_csv(directory_name + product_file)

    customers_items, customers_count, customers_error_count = \
        import_csv(directory_name + customers_file)

    rental_items, rental_count, rental_error_count = \
        import_csv(directory_name + rental_file)

    mongo = MongoDBConnection()

    with mongo:
        hpn_db = mongo.connection.HPNorton
        product = hpn_db['product']
        customers = hpn_db['customers']
        rental = hpn_db['rental']

        product.insert_many(product_items)
        customers.insert_many(customers_items)
        rental.insert_many(rental_items)

    return (product_count, customers_count, rental_count),\
           (product_error_count, customers_error_count, rental_error_count)


@logger_decorator
def import_csv(file_path):
    """Reads csv file into a dictionary"""

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
        # logging.error('Error: {}'.format(identifier))

    return dict_list, record_count, error_count


@logger_decorator
def show_available_products():
    """Lists all available products for rent (quantity_available > 0)"""
    mongo = MongoDBConnection()

    with mongo:
        hpn_db = mongo.connection.HPNorton
        product = hpn_db['product']

        product_cursor = product.find({'quantity_available': {'$gt': '0'}},
                                      {'_id': 0,
                                       'product_id': 1,
                                       'description': 1,
                                       'product_type': 1,
                                       'quantity_available': 1}
                                      ).sort('product_id', pymongo.ASCENDING)

        available_products = []
        for product in product_cursor:
            available_products.append(product)

    return available_products


@logger_decorator
def show_rentals(user_id=''):
    """Shows all rental by user_id"""
    mongo = MongoDBConnection()

    with mongo:
        hpn_db = mongo.connection.HPNorton
        rental = hpn_db['rental']

        rental_cursor = rental.find({'user_id': user_id},
                                    {'_id': 0,
                                     'product_id': 1,
                                     'user_id': 1}
                                    ).sort('product_id', pymongo.ASCENDING)

        rentals = []
        for rental in rental_cursor:
            rentals.append(rental)

    return rentals


@logger_decorator
def show_customers():
    """Shows all customers by user_id"""
    mongo = MongoDBConnection()

    with mongo:
        hpn_db = mongo.connection.HPNorton

        customers = hpn_db['customers']
        customers_cursor = customers.find({},
                                          {'_id': 0,
                                           'user_id': 1,
                                           'name': 1,
                                           'address': 1,
                                           'zip_code': 1,
                                           'phone_number': 1,
                                           'e-mail': 1
                                           }).sort('user_id',
                                                   pymongo.ASCENDING)

        customers = []
        for customer in customers_cursor:
            customers.append(customer)

    return customers


@logger_decorator
def drop_collections():
    """Deletes existing DB colletions"""
    mongo = MongoDBConnection()

    with mongo:
        hpn_db = mongo.connection.HPNorton
        hpn_db['product'].drop()
        hpn_db['customers'].drop()
        hpn_db['rental'].drop()


if __name__ == '__main__':
    # START_FRESH = input("Start with empty collections? (Y/N)")
    START_FRESH = True

    FILE_PATH = 'data/'
    import_data(FILE_PATH, 'product.csv', 'customers.csv', 'rental.csv',
                START_FRESH)

    show_available_products()
    show_rentals('user002')
    show_customers()

