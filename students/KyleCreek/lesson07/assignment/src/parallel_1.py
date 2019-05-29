import csv
from pymongo import MongoClient
import logging
import datetime as dt
from multiprocessing import Pool
import threading
import queue

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


def mongo_processor(target_db_name, db_content, out_queue):
    """
    Processes information with a Mongo Database
    :param target_db_name: Desired database name
    :param db_content: Content to store inside databse
    :param out_queue: Queue to store information
    :return: list containing the files processed and time
    taken to process data
    """

    mongo = MongoDbConnection()


    with mongo:
        database = mongo.connection.Lesson07DB_2


        # Count initial records
        target_db = database[target_db_name]
        initial_count = target_db.count_documents({})
        out_queue.put(initial_count)

        total_process = len(db_content)
        out_queue.put(total_process)

        # Add Records
        target_db.insert_many(db_content)

        # Count final records
        final_count = target_db.count_documents({})
        out_queue.put(final_count)

        end_time = dt.datetime.now()
        out_queue.put(end_time)

    return [initial_count, final_count, end_time]


if __name__ == "__main__":

    start = dt.datetime.now()

    # --- Define File Names --- #
    directory_name = "C:\\Python220A_2019\\students\\KyleCreek\\lesson07\\assignment\\data\\"
    product_file = "product.csv"
    customer_file = "customer.csv"


    # Create file path for directory
    product_file_directory = directory_name + product_file
    customer_file_directory = directory_name + customer_file

    directory_list = [product_file_directory,
                      customer_file_directory]

    # --- Import CSV Files --- #
    # Note: This Section is acceptable
    with Pool(processes=2) as p:
        return_lists = p.map(csv_importer, directory_list)

    product_dicts_1 = return_lists[0]
    customer_dicts_1 = return_lists[1]

    # Establish return lists
    prod_return = []
    cust_return = []


    # Esablish Queues
    prod_queue = queue.Queue()
    cust_queue = queue.Queue()


    # Esatblish Threads
    prod_thread =threading.Thread(target=mongo_processor, args=('products', product_dicts_1, prod_queue))
    cust_thread = threading.Thread(target=mongo_processor, args=('customers', customer_dicts_1, cust_queue))

    # Start Threads
    prod_thread.start()
    cust_thread.start()

    # Join Threads
    prod_thread.join()
    cust_thread.join()

    # Lists to store return data
    prod_return = []
    cust_return = []

    # Empty the Queues
    while not prod_queue.empty():
        prod_return.append(prod_queue.get())

    while not cust_queue.empty():
        cust_return.append(cust_queue.get())

    end = dt.datetime.now()
    prod_tuple = (prod_return[0],
                  prod_return[1],
                  prod_return[2],
                  (prod_return[3]-start).total_seconds())
    print(prod_tuple)
    cust_tuple = (cust_return[0],
                  cust_return[1],
                  cust_return[2],
                  (cust_return[3]-start).total_seconds())

    print(cust_tuple)
    print((end-start).total_seconds())
