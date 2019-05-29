# ----------------------------- #
# Title:
# Desc:
# Change Log: (Who, When, What)
# ----------------------------- #
import csv
from pymongo import MongoClient
import logging
import datetime as dt
logging.basicConfig(level=logging.DEBUG)


class MongoDbConnection(object):
    """
    Class Established Connection to a Mongo Database
    """
    def __init__(self, host='127.0.0.1', port=27017):
        self.host = host
        self.port = port
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient(self.host, self.port)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


def csv_importer(filepath):
    """
    Function takes file path of .csv file and returns a
    list of dictionaries from .csv file
    :param file path: file path directory of target .csv File
    :return: List of dictionaries derived from provided file
    path
    """
    with open(filepath, 'r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        dict_list = []
        for line in reader:
            dict_list.append(line)

    return dict_list


def mongo_processor(target_db_name, db_content):
    """
    Processes data into Mongo Database
    :param target_db_name: Targeted Database Name
    :param db_content: Content to be added to targeted database
    :return: List containing counts
    """

    mongo = MongoDbConnection()


    with mongo:
        database = mongo.connection.Lesson07DB_1


        # Count initial records
        target_db = database[target_db_name]
        initial_count = target_db.count_documents({})

        # Add Records
        target_db.insert_many(db_content)

        # Count final records
        final_count = target_db.count_documents({})

    return [initial_count, final_count]


def profiler(file_path, db_name):
    """
    Profiles the execution of interaction with a Mongo Database
    :param file_path: Desired file path
    :param db_name: Name of database to interact with
    :return: Tuple containing various items
    """

    start_time = dt.datetime.now()
    db_list = csv_importer(file_path)
    db_process_count = len(db_list)
    db_return = mongo_processor(db_name, db_list)
    elapsed_time = (dt.datetime.now() - start_time).total_seconds()
    return_data = (db_process_count,
                   db_return[0],
                   db_return[1],
                   elapsed_time)

    return return_data


if __name__ == "__main__":

    start = dt.datetime.now()

    # --- Define File Names --- #
    directory_name = "C:\\Python220A_2019\\students\\KyleCreek\\lesson07\\assignment\\data\\"
    product_file = "product.csv"
    customer_file = "customer.csv"


    # Create file path for directory
    product_file_directory = directory_name + product_file
    customer_file_directory = directory_name + customer_file

    products_info = profiler(product_file_directory, 'products')
    customers_info = profiler(customer_file_directory, 'customers')

    total_time = (dt.datetime.now() - start).total_seconds()
    print(products_info)
    print(customers_info)
    logging.info("Total Elapsed Time: {}".format(total_time))
