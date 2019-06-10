"""
# Title: database.py
# Desc: performs the actions required of lesson05
# Assignment04
# Change Log: (Who, When, What)
# KCreek, 5/1/2019, Created initial Script
# KCreek, 5/7/2019, Finished Initial Script
# KCreek, 6/9/2019, Re-Wrote to complete Lesson10
"""
import csv
from pymongo import MongoClient
import time
import datetime

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


def timer_function(orig_function):
    """
    Performs timing actions to complete each function
    :return: Decorates function and writes information
    to file.
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        returned_value = orig_function(*args, **kwargs)
        end = time.time() - start

        # Calculate number of Records Processed
        processed = len(args) + len(kwargs)

        # Join Writeable Text
        text = '{}: {} ran in {} seconds, processing {} records'.format(
            datetime.datetime.now(),
            orig_function.__name__,
            end,
            processed)

        # Write Data to a file
        with open("timings.txt", 'a+') as file:
            file.write(text + '\n')
        return returned_value

    return wrapper



@timer_function
def show_available_products():
    """
    Returns a python dictionary of products listed
    as available
    :return: Dictionary with certain fields.
    """
    # Create a connection to the server
    mongo = MongoDbConnection()

    with mongo:
        # connect to database
        data_base = mongo.connection.NortonDB2

        # Enter the products database and collect all data
        collection = data_base['products']

        # Query Database for objects in collection and add to list
        available_products_list = []
        for dictionary in collection.find():
            if int(dictionary['quantity_available']) > 0:
                available_products_list.append(dictionary['ï»¿product_id'])
    return available_products_list

@timer_function
def show_rentals(product_id):
    """
    Returns a Python dictionary with user information
    from users that have rented products matching
    product_id
    :param product_id: User Product ID
    :return: Dictionary with user information
    """
    # Create a connection to the Server
    mongo = MongoDbConnection()

    with mongo:
        # Connect to the Database
        data_base = mongo.connection.NortonDB2

        # Enter the rentals db
        collection_rentals = data_base['rentals']

        # Enter the Customers Database
        collection_users = data_base['customers']

        # list to store all the matched users
        match_users_list = []
        # Query Rentals Database for all records that match that I need to query ID
        for dictionary in collection_rentals.find():
            if dictionary['ï»¿product_id'] == product_id:
                match_users_list.append(dictionary['user_id'])

        # List to store the dictionaries of user info
        user_info_dictionary_list = []

        # Query the matched users list to store into list
        for name in match_users_list:
            user_info_dictionary_list.append(
                collection_users.find_one({'ï»¿user_id': name}))

        return user_info_dictionary_list

@timer_function
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

@timer_function
def database_maker(dict_list, db_name):
    """
    Takes a list of dictionaries and creates a
    Collection in a target mongo Database
    :param dict_list: list containing dictionary of information
    :param db_name: String for collection name
    :return: None
    """
    mongo = MongoDbConnection()
    with mongo:

        # Create a database
        database = mongo.connection.NortonDB #NortonDB/NortonDB1/NortonDB2

        # Create a collection within the Database
        target_db = database[db_name]

        # Insert Data into Database
        target_db.insert_many(dict_list)

        return_records = target_db.count_documents({})

    return return_records

@timer_function
def import_data(directory_name, product_file, customer_file, rentals_file):
    """
    Function takes a directory name three .csv files as input, one with
    product data, one with customer data, and the third one with rentals
    data and creates and populates a new MongoDB database with these
    data. It returns 2 tuples; the first with a record count of the
    number of products, customers, and rentals added, the second
    with a count of any errors that occurred
    :param directory_name: filepath for directory name
    :param product_file: file name for product file
    :param customer_file: file  name for customer file
    :param rentals_file: file name for rentals file
    :return: Tuple containing above noted data and number
    of errors.
    """
    # Counts number of exceptions that occurred
    exception_counter = 0
    try:
        # establish directory files
        product_file_directory = directory_name + product_file
        customer_file_directory = directory_name + customer_file
        rentals_file_directory = directory_name + rentals_file

        # Obtain Dictionaries from Directories
        prod_dict = csv_importer(product_file_directory)
        customer_dict = csv_importer(customer_file_directory)
        rentals_dict = csv_importer(rentals_file_directory)

        # Create List containing Dictionaries for database creation
        dict_list = [prod_dict,
                     customer_dict,
                     rentals_dict
                     ]

        # Create a list containing target database names
        db_name_list = ['products',
                        'customers',
                        'rentals'
                        ]

        # Create Databases with each dictionary and associated name
        db_counter = 0
        # Need Error Counter
        return_records_tuple = ()
        while db_counter < 3:
            record_number = database_maker(dict_list[db_counter],
                                           db_name_list[db_counter])
            return_records_tuple = return_records_tuple + (record_number,)
            db_counter += 1

        return_records_tuple = return_records_tuple + (exception_counter,)

        return return_records_tuple
    except Exception as e:
        print(e)
        exception_counter += 1
        return return_records_tuple



