"""
database.py
A compilation of methods to interact with a MongoDB DB
"""
from src.mongodb import MongoDBConnection
from pymongo.errors import BulkWriteError
import logging
import pandas as pd
import os


def init_logging():
    """ Setting up the logger
        Logging to a file called db.log with anything INFO and above
    """
    logger = logging.getLogger(__name__)
    log_format = (
        "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s")
    log_file = 'db.log'
    formatter = logging.Formatter(log_format)
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)

    return logger


LOGGER = init_logging()
MONGO = MongoDBConnection()


def import_data(directory_name, product_file, customer_file, rentals_file):
    """import_data(directory_name, product_file, customer_file, rentals_file)

    Given a directory and 3 filenames, create a collection for each and
    add the corresponding csv data to their respective collection.

    :param directory_name str: Name of the dir where your CSV files are located
    :param product_file str: Name of the product CSV file
    :param customer_file str: Name of the customer CSV file
    :param rentals_file str: Name of the rentals CSV file

    :return 2 tuples, one showing total records added for each collection
                      one showing total errors that occured for each add
    :rtype tuple
    """
    with MONGO:
        try:
            db = MONGO.connection.db
            products_col, customers_col, rentals_col = (db['products'],
                                                        db['customers'],
                                                        db['rentals'])
            csvs = [product_file, customer_file, rentals_file]
            data_dir = os.listdir(os.path.abspath(directory_name))
            records = []
            errors = []
            for csv in csvs:
                if csv in data_dir:
                    if csv == product_file:
                        try:
                            LOGGER.info("CSV file is a {csv}")
                            errors_count = 0
                            csv_list = []
                            csv_dict = pd.read_csv(
                                os.path.abspath(
                                    directory_name + '/' + csv)).to_dict(
                                        orient='records')
                            for row in csv_dict:
                                id = row.pop('product_id')
                                row['_id'] = id
                                csv_list.append(row)
                            result = db.products_col.insert_many(
                                csv_list, ordered=True)
                            records.append(len(result.inserted_ids))
                            LOGGER.info("Total records from %s are: %s",
                                        csv, len(result.inserted_ids))
                        except BulkWriteError:
                            errors_count += 1
                        errors.append(errors_count)
                    elif csv == customer_file:
                        try:
                            LOGGER.info("CSV file is a {csv}")
                            errors_count = 0
                            csv_list = []
                            csv_dict = pd.read_csv(
                                os.path.abspath(
                                    directory_name + '/' + csv)).to_dict(
                                        orient='records')
                            for row in csv_dict:
                                id = row.pop('user_id')
                                row['_id'] = id
                                csv_list.append(row)
                            result = db.customers_col.insert_many(
                                csv_list, ordered=True)
                            records.append(len(result.inserted_ids))
                            LOGGER.info("Total records from %s are: %s",
                                        csv, len(result.inserted_ids))
                        except BulkWriteError:
                            errors_count += 1
                        errors.append(errors_count)

                    elif csv == rentals_file:
                        try:
                            LOGGER.info("CSV file is a {csv}")
                            errors_count = 0
                            csv_list = []
                            csv_dict = pd.read_csv(
                                os.path.abspath(
                                    directory_name + '/' + csv)).to_dict(
                                        orient='records')
                            result = db.rentals_col.insert_many(
                                csv_dict, ordered=True)
                            records.append(len(result.inserted_ids))
                            LOGGER.info("Total records from %s are: %s",
                                        csv, len(result.inserted_ids))
                        except BulkWriteError:
                            errors_count += 1
                        errors.append(errors_count)
        except Exception as error:
            LOGGER.error("Error: %s", error)
        finally:
            return tuple(records), tuple(errors)


def show_available_products():
    """show_available_products()

    Grab all products with a quantity field higher than 0
    and return as a dict with specified fields.

    :return dict of products listed as available
    :rtype dict
    """
    try:
        with MONGO:
            db = MONGO.connection.db
            avail_product = {}
            result = db.products_col.find(
                {"quantity_available":{'$gt': 0}},
                {"description": 1, "product_type": 1,
                 "quantity_available": 1, "_id": 1})
            for row in result:
                p_id = row.pop('_id')
                avail_product[p_id] = row
        LOGGER.info("Available Products: %s", avail_product)
        return avail_product
    except Exception as error:
        LOGGER.error("Error: %s", error)

def show_rentals(product_id):
    """show_rentals(product_id)
    Returns a Python dictionary with the following user information
    from users that have rented products matching product_id:
        - user_id
        - name
        - address
        - phone_number
        - email

    :params product_id int: Product ID of product to show rentals for

    :return dict of users associated with product_id
    :rtype dict
    """
    try:
        with MONGO:
            db = MONGO.connection.db
            customers = {}
            result = db.get_collection("rentals_col").aggregate(
                [{"$lookup": {"from": "customers_col",
                              "localField": "user_id",
                              "foreignField": "_id",
                              "as": "rentals"}},
                 {"$match": {"product_id": product_id}}])
            count = 0
            for row in result:
                count += 1
                id = f"C00{count}"
                row.pop('_id'), row.pop('product_id')
                customers[id] = row
        LOGGER.info("Customers w/ Rentals: %s", customers)
        return customers
    except Exception as error:
        LOGGER.error("Error: %s", error)

def drop_cols(*args):
    """drop_cols(*args)
    Drop collections based on inputed values in DB

    :param args tuple: Tuple of collections name in DB to drop

    :return None
    :rtype None
    """
    with MONGO:
        db = MONGO.connection.db
        for col in args:
            db.drop_collection(col)
