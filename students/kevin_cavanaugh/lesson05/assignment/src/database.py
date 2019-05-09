#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient
import csv


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
        self.connection = MongoClient(self.host, self.port)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


def csv_to_list_of_dict(csv_file):
    with open(csv_file, encoding='utf-8-sig') as file:
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


def show_available_products():
    mongo = MongoDBConnection()
    with mongo:
        db = mongo.connection.HP_NORTON_DB
        products = db['Products']

        available_products = {}
        for document in products.find({'quantity_available': {'$ne': '0'}}):
            available_products[document['product_id']] = {
                'description': document['description'],
                'product_type': document['product_type'],
                'quantity_available': document['quantity_available']
            }
    return available_products


def show_rentals(product_id, database):
    mongo = MongoDBConnection()
    with mongo:
        db = mongo.connection[database]
        rentals = db['Rentals']
        customers = db['Customers']

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


def drop_collections(*collection_names, database):
    mongo = MongoDBConnection()
    with mongo:
        db = mongo.connection[database]
        [db.drop_collection(collection) for collection in collection_names]


def main():

    product_file = '../data/product.csv'
    rental_file = '../data/rental.csv'
    customers_file = '../data/customers.csv'
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

