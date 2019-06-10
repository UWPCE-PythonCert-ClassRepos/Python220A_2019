#!/usr/bin/env python3
''' Stores and retrieves data from a rentals db '''

import os
from timeit import default_timer as timer
import pymongo

CLIENT = pymongo.MongoClient('localhost', 27017)
DB = CLIENT.data
LOG_FILE = 'timing.log'

def log_timing(func_name, time, rows=0):
    ''' A quick function to log timings to a file '''
    with open(LOG_FILE, 'a+') as fhand:
        fhand.write("Function=%s timing=%s rows=%s\n" % (func_name, time, rows))

def timing_logger_standard(row_hint):
    ''' Decorator for standard functions with fixed or no rows '''
    def wrap(func):
        ''' The inner decorator in a decorator with args '''
        def add_timing(*args):
            ''' The actual decorating function '''
            start = timer()
            (data) = func(*args)
            end = timer()
            timing = end - start
            log_timing(func.__name__, timing, row_hint)
            return data
        return add_timing
    return wrap

def timing_logger_find(func):
    ''' Decorator for functions which find rows '''
    def add_timing(*args):
        ''' The decorating function '''
        start = timer()
        data = func(*args)
        end = timer()
        timing = end - start
        log_timing(func.__name__, timing, len(data))
        return data
    return add_timing

def timing_logger_import(func):
    ''' Decorator for functions which import rows from csv '''
    def add_timing(*args):
        ''' The decorating function '''
        start = timer()
        (records, errors) = func(*args)
        end = timer()
        timing = end - start
        log_timing(func.__name__, timing, records + errors)
        return (records, errors)
    return add_timing

@timing_logger_standard('N/A')
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

@timing_logger_standard('N/A')
def import_data(dirname, products, customers, rentals):
    ''' Imports data from a bunch of csv files located at dirname '''
    prod_rec_errs = import_csv_data(PRODUCTS, os.path.join(dirname, products))
    cust_rec_errs = import_csv_data(CUSTOMERS, os.path.join(dirname, customers))
    rent_rec_errs = import_csv_data(RENTALS, os.path.join(dirname, rentals))
    zipped = list(zip(prod_rec_errs, cust_rec_errs, rent_rec_errs))
    return zipped

@timing_logger_standard(1)
def insert_row(collection, row):
    ''' Inserts a row into DB. Returns True on success, else False '''
    try:
        collection.insert_one(row)
    except pymongo.errors.PyMongoError as err:
        print("Failure to write row to db. %s - %s", row, err)
        return False
    return True

@timing_logger_import
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

@timing_logger_find
def show_available_products():
    ''' returns all available products (quantity isn't 0) '''
    prods = {}
    for product in PRODUCTS.find({'quantity_available': {'$ne': "0"}}):
        product_id = product.pop('product_id')
        product.pop('_id')
        prods[product_id] = product
    return prods

@timing_logger_find
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
