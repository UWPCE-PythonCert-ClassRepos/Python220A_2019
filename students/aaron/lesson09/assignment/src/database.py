#!/usr/bin/env python3
''' Stores and retrieves data from a rentals db '''

import os
from contextlib import contextmanager
import pymongo

HOSTNAME = 'localhost'
PORT = 27017

# Simple generator style context manager
@contextmanager
def open_collection(name, host, port):
    ''' opens a db client connection yields a collection '''
    client = pymongo.MongoClient(host, port)
    dbdata = client.data
    collection = dbdata[name]
    yield collection
    client.close()

def setup_db():
    ''' sets up the database and collections '''
    with open_collection('products', HOSTNAME, PORT) as coll:
        coll.drop()
        coll.create_index([('product_id', pymongo.ASCENDING)], unique=True)
    with open_collection('customers', HOSTNAME, PORT) as coll:
        coll.drop()
        coll.create_index([('user_id', pymongo.ASCENDING)], unique=True)
    with open_collection('rentals', HOSTNAME, PORT) as coll:
        coll.drop()

def import_data(dirname, products, customers, rentals):
    ''' Imports data from a bunch of csv files located at dirname '''
    prod_rec_errs = import_csv_data('products', os.path.join(dirname, products))
    cust_rec_errs = import_csv_data('customers', os.path.join(dirname, customers))
    rent_rec_errs = import_csv_data('rentals', os.path.join(dirname, rentals))
    zipped = list(zip(prod_rec_errs, cust_rec_errs, rent_rec_errs))
    return zipped

def insert_row(collection_name, row):
    ''' Inserts a row into DB. Returns True on success, else False '''
    try:
        with open_collection(collection_name, HOSTNAME, PORT) as coll:
            coll.insert_one(row)
    except pymongo.errors.PyMongoError as err:
        print("Failure to write row to db. %s - %s", row, err)
        return False
    return True

def import_csv_data(collection, path):
    ''' Imports csv data from a file, returns (records, failures) '''
    columns = []
    records = 0
    errors = 0
    try:
        with open(path, encoding="ISO-8859-1") as fhand:
            # retrieve the csv header
            header = fhand.readline().rstrip()
            columns = header.split(',')

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
    for row in rows:
        success = insert_row(collection, row)
        if success:
            records += 1
        else:
            errors += 1
    return (records, errors)

def show_available_products():
    ''' returns all available products (quantity isn't 0) '''
    prods = {}
    with open_collection('products', HOSTNAME, PORT) as coll:
        for product in coll.find({'quantity_available': {'$ne': "0"}}):
            product_id = product.pop('product_id')
            product.pop('_id')
            prods[product_id] = product
    return prods

def show_rentals(product_id):
    ''' returns all of the customers who rented a product '''
    rents = {}
    with open_collection('rentals', HOSTNAME, PORT) as rent_coll:
        with open_collection('customers', HOSTNAME, PORT) as cust_coll:
            for rent in rent_coll.find({'product_id': product_id}):
                for customer in cust_coll.find({'user_id': rent['user_id']}):
                    cust_id = customer.pop('user_id')
                    customer.pop('_id')
                    rents[cust_id] = customer
    return rents

setup_db()
