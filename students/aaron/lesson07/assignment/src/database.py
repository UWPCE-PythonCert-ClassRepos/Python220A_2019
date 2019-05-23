#!/usr/bin/env python3
''' Stores and retrieves data from a rentals db '''

import os
import threading
import pymongo

CLIENT = pymongo.MongoClient('localhost', 27017)
DB = CLIENT.data

def setup_db(database):
    ''' sets up the collections and returns them '''
    products = database.products
    products.drop()
    products.create_index([('product_id', pymongo.ASCENDING)], unique=True)
    customers = database.customers
    customers.drop()
    customers.create_index([('user_id', pymongo.ASCENDING)], unique=True)
    rentals = database.rentals
    rentals.drop()
    return (products, customers, rentals)

def import_data(dirname, products, customers, rentals):
    ''' Imports data from a bunch of csv files located at dirname '''
    prod_rec_errs = import_csv_data(PRODUCTS, os.path.join(dirname, products))
    cust_rec_errs = import_csv_data(CUSTOMERS, os.path.join(dirname, customers))
    rent_rec_errs = import_csv_data(RENTALS, os.path.join(dirname, rentals))
    zipped = list(zip(prod_rec_errs, cust_rec_errs, rent_rec_errs))
    return zipped

def insert_row(collection, row, successes):
    ''' Inserts a row into DB. Returns True on success, else False '''
    try:
        collection.insert_one(row)
    except pymongo.errors.PyMongoError as err:
        print("Failure to write row to db. %s - %s", row, err)
        successes.append(False)
        return
    successes.append(True)
    return

def import_csv_data(collection, path):
    ''' Imports csv data from a file, returns (records, failures) '''
    columns = []
    records = 0
    errors = 0
    try:
        with open(path, encoding="ISO-8859-1") as fhand:
            # retrieve the csv header
            columns = fhand.readline().rstrip().split(',')

            # retrieve each row and populate data
            rows = []
            for line in fhand:
                fields = line.rstrip().split(',')
                row = {}
                for field in enumerate(fields):
                    row[columns[field[0]]] = field[1]
                rows.append(row)
    except Exception as err:
        print('Failure to read data from %s: %s', path, err)
        raise err

    # could have used a queue here but ran with a list instead
    successes = []
    # a list for the thread objects
    threads = []

    # set up a new thread for each row to insert
    # (this may be crazy for large datasets)
    for row in rows:
        threads.append(threading.Thread(target=insert_row,
                                        args=(collection, row, successes)))

    # start all the threads, then wait until they complete
    # tried to use a comprehension here, but pylint didn't like it
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    # count the successes and the errors
    records = len([success for success in successes if success])
    errors = len([success for success in successes if not success])
    return (records, errors)

def show_available_products():
    ''' returns all available products (quantity isn't 0) '''
    prods = {}
    for product in PRODUCTS.find({'quantity_available': {'$ne': "0"}}):
        product_id = product.pop('product_id')
        product.pop('_id')
        prods[product_id] = product
    return prods

def show_rentals(product_id):
    ''' returns all of the customers who rented a product '''
    rents = {}
    for rent in RENTALS.find({'product_id': product_id}):
        for customer in CUSTOMERS.find({'user_id': rent['user_id']}):
            cust_id = customer.pop('user_id')
            customer.pop('_id')
            rents[cust_id] = customer
    return rents

PRODUCTS, CUSTOMERS, RENTALS = setup_db(DB)
