"""
database.py
A compilation of methods to interact with a MongoDB DB
"""
import os
import logging
import pandas as pd
from pymongo.errors import BulkWriteError
from src.mongodb import MongoDBConnection


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
    file_handler.setLevel(logging.INFO)
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
            database = MONGO.connection.db
            products_col, customers_col, rentals_col = (database['products'],
                                                        database['customers'],
                                                        database['rentals'])
            csvs = [product_file, customer_file, rentals_file]
            LOGGER.info('CSV files: %s', csvs)
            data_dir = os.listdir(os.path.abspath(directory_name))
            records = []
            errors = []
            file_dict = {'product.csv': products_col,
                         'customers.csv': customers_col,
                         'rental.csv': rentals_col}
            for csv in csvs:
                if csv in data_dir:
                    collection = file_dict[csv]
                    try:
                        LOGGER.info("CSV file is a {csv}")
                        errors_count = 0
                        csv_list = csv_to_list_dict(directory_name, csv)
                        result = collection.insert_many(
                            csv_list, ordered=True)
                        records.append(len(result.inserted_ids))
                        LOGGER.info("Total records from %s are: %s",
                                    csv, len(result.inserted_ids))
                    except BulkWriteError as error:
                        LOGGER.error("Bulk write issue: %s", error.details)
                        print(error.details)
                        errors_count += 1
                    errors.append(errors_count)
        except Exception as error:
            LOGGER.error("Error: %s", error)
        finally:
            return tuple(records), tuple(errors)


def csv_to_list_dict(directory_name, csv):
    """csv_to_list_dict(directory_name, csv)

    Given a directory and a csv file, read the CSV and convert it to
    a dict and add it into the returned list.

    :param directory_name str: Name of the dir where your CSV files are located
    :param csv str: Name of the CSV file

    :return list containing a dict values of the CSV data
    :rtype list
    """
    LOGGER.info("CSV file is a {csv}")
    csv_list = []
    csv_dict = pd.read_csv(
        os.path.abspath(
            directory_name + '/' + csv)).to_dict(
                orient='records')
    for row in csv_dict:
        if csv != "rental.csv":
            db_id = row.pop(list(row.keys())[0])
            row['_id'] = db_id
        csv_list.append(row)
    return csv_list


def show_available_products():
    """show_available_products()

    Grab all products with a quantity field higher than 0
    and return as a dict with specified fields.

    :return dict of products listed as available
    :rtype dict
    """
    try:
        with MONGO:
            database = MONGO.connection.db
            avail_product = {}
            result = database.products.find(
                {"quantity_available": {'$gt': 0}},
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
            database = MONGO.connection.db
            customers = {}
            result = database.get_collection("rentals").aggregate(
                [{"$lookup": {"from": "customers",
                              "localField": "user_id",
                              "foreignField": "_id",
                              "as": "rental"}},
                 {"$match": {"product_id": product_id}}])
            count = 0
            for row in result:
                count += 1
                db_id = f"C00{count}"
                row.pop('_id')
                row.pop('product_id')
                customers[db_id] = row
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
        database = MONGO.connection.db
        for col in args:
            database.drop_collection(col)