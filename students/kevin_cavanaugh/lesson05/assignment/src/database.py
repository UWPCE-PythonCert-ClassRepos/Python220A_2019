#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient
import csv
from pymongo import errors

class MongoDBConnection():
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
        self.connection = MongoClient(self.host, self.port)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


def csv_to_list_of_dict(csv_file):
    with open(csv_file) as file:
        reader = csv.reader(file)
        l = [row for row in reader]
        header = l[0]
        mongo_insert = []
        header_index = 0
        for rows in l[1:]:
            item_dict = {}
            for item in rows:
                item_dict[header[header_index]] = item
                header_index += 1
            mongo_insert.append(item_dict)
            header_index = 0

        return mongo_insert


def import_data(product_file, customer_file, rentals_file):
    """
    import data from csv to mongoDB
    """
    mongo = MongoDBConnection()
    products_list = csv_to_list_of_dict(product_file)
    customers_list = csv_to_list_of_dict(customer_file)
    rentals_list = csv_to_list_of_dict(rentals_file)
    with mongo:
        db = mongo.connection.HP_NORTON_DB
        products = db['Products']
        products.insert_many(products_list)
        customers = db['Customers']
        customers.insert_many(customers_list)
        rentals = db['Rentals']
        rentals.insert_many(rentals_list)

        collections_inserted = (products.count_documents({}),
                                customers.count_documents({}),
                                rentals.count_documents({}))

        collections_invalid = (products.errors.count_documents({}),
                               customers.errors.count_documents({}),
                               rentals.errors.count_documents({}))

        return collections_inserted, collections_invalid


def main():

    product_file = '../data/product.csv'
    rental_file = '../data/rental.csv'
    customers_file = '../data/customers.csv'
    print(import_data(product_file, customers_file, rental_file))

if __name__ == '__main__':
    main()

