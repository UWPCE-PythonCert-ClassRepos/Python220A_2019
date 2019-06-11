"""
assignment 10
update: assignment 5 database.py
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
from pymongo import MongoClient
from pymongo import errors
import time
from datetime import datetime


class MongoDBConnection:
    """
    MongoDB connection to server
    """

    def __init__(self, host='127.0.0.1', port=27017):
        """
        initialize host, port & connection
        be sure to use the ip address not name for local windows
        """
        self.host = host
        self.port = port
        self.connection = None

    def __enter__(self):
        """
        Connect to a MongoDB
        """
        self.connection = MongoClient(self.host, self.port)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Close DB Connection
        """
        self.connection.close()


def timer(func):
    """
     decorator utilized to time functions & record records processed
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time() - start

        records_processed = len(args) + len(kwargs)

        output_txt = f'{datetime.now()}: {func.__name__} processed ' \
            f'{records_processed} in {end} seconds'

        with open('timings.txt', 'a+') as file:
            file.write(output_txt + '\n')
        return value
    return wrapper


@timer
def csv_to_list_of_dict(csv_file):
    """
    turn csv file to dict
    """
    with open(csv_file, encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        item_list = [row for row in reader]
        header = item_list[0]
        mongo_insert = []
        header_index = 0
        for rows in item_list[1:]:
            item_dict = {}
            for item in rows:
                item_dict[header[header_index]] = item
                header_index += 1
            mongo_insert.append(item_dict)
            header_index = 0

        return mongo_insert


@timer
def import_data(product_file, customer_file, rentals_file):
    """
    import data from csv to mongoDB
    """
    mongo = MongoDBConnection()
    products_list = csv_to_list_of_dict(product_file)
    customers_list = csv_to_list_of_dict(customer_file)
    rentals_list = csv_to_list_of_dict(rentals_file)
    with mongo:
        database = mongo.connection.HP_NORTON_DB

        products_insert_errors = 0
        try:
            products = database['Products']
            products.insert_many(products_list)
        except errors.CollectionInvalid:
            products_insert_errors += 1

        customers_insert_errors = 0
        try:
            customers = database['Customers']
            customers.insert_many(customers_list)
        except errors.CollectionInvalid:
            customers_insert_errors += 1

        rentals_insert_errors = 0
        try:
            rentals = database['Rentals']
            rentals.insert_many(rentals_list)
        except errors.CollectionInvalid:
            rentals_insert_errors += 1

        collections_inserted = (products.count_documents({}),
                                customers.count_documents({}),
                                rentals.count_documents({}))

        collections_invalid = (products_insert_errors,
                               customers_insert_errors,
                               rentals_insert_errors)

        return collections_inserted, collections_invalid


@timer
def show_available_products():
    """
    show available products
    """
    mongo = MongoDBConnection()
    with mongo:
        database = mongo.connection.HP_NORTON_DB
        products = database['Products']

        available_products = {}
        for document in products.find({'quantity_available': {'$ne': '0'}}):
            available_products[document['product_id']] = {
                'description': document['description'],
                'product_type': document['product_type'],
                #'quantity_available': document['quantity_available']
            }
    return available_products


@timer
def show_rentals(product_id, database):
    """
    show rentals
    """
    mongo = MongoDBConnection()
    with mongo:
        database = mongo.connection[database]
        rentals = database['Rentals']
        customers = database['Customers']

        rentals_available = {}
        for product in rentals.find({'product_id': product_id}):
            for customer in customers.find({'user_id': product['user_id']}):
                rentals_available[product['user_id']] = {
                    'name': customer['name'],
                    'address': customer['address'],
                    'phone_number': customer['phone_number'],
                    'email': customer['email']
                }

    return rentals_available


@timer
def drop_collections(*collection_names, database):
    """
    drop collections
    """
    mongo = MongoDBConnection()
    with mongo:
        database = mongo.connection[database]
        [database.drop_collection(collection) for collection in collection_names]

    return True


@timer
def main():
    """
    main
    """

    product_file = r'C:\Python220\Python220A_2019\students\kevin_cavanaugh\lesson10\assignment\data\product.csv'
    rental_file = r'C:\Python220\Python220A_2019\students\kevin_cavanaugh\lesson10\assignment\data\rental.csv'
    customers_file = r'C:\Python220\Python220A_2019\students\kevin_cavanaugh\lesson10\assignment\data\customer.csv'
    print('\n')
    print("******* Products, Customers, Rentals Imported (Errors) *********")
    print(import_data(product_file, customers_file, rental_file))
    print('\n')
    print("******* AVAILABLE PRODUCTS *****")
    print(show_available_products())
    print('\n')
    print("******* PRODUCT RENTALS BY PRODUCT ID **********")
    print(show_rentals('prd005',
                       database='HP_NORTON_DB'))

    drop_collections('Products', 'Customers', 'Rentals',
                     database='HP_NORTON_DB')


if __name__ == '__main__':
    main()
