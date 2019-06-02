"""
parallel.py
A compilation of methods to interact with a MongoDB DB
"""
import os
import logging
import datetime
import threading
import pandas as pd
from pymongo.errors import BulkWriteError
from src.mongodb import MongoDBConnection


def init_logging():
    """Setting up the logger.
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


def import_data(directory_name, csv):
    """import_data(directory_name, csv)

    Given a directory and filename, create a collection and
    add the corresponding csv data to their respective collection.

    :param directory_name str: Name of the dir where your CSV files are located
    :param csv str: Name of the CSV file

    :return 1 tuple with 4 values,
            one showing total records added for each collection
            one showing total record count in db prior to running
            one showing total record count after running
            one showing total time to run the module
    :rtype tuple
    """
    records = []
    errors = []
    record_count_before_op = None
    record_count_after_op = None
    with MONGO:
        start = datetime.datetime.now()
        try:
            database = MONGO.connection.db
            file_name = csv.rstrip('.csv')
            col = database[file_name]
            LOGGER.info('CSV file: %s', csv)
            data_dir = os.listdir(os.path.abspath(directory_name))

            if csv in data_dir:
                collection = col
                record_count_before_op = collection.count()
                try:
                    LOGGER.info("CSV file is {csv}")
                    errors_count = 0
                    csv_list = csv_to_list_dict(directory_name, csv)
                    result = collection.insert_many(
                        csv_list, ordered=True)
                    records.append(result.inserted_ids)
                    LOGGER.info("Total records from %s are: %s",
                                csv, len(result.inserted_ids))
                    record_count_after_op = collection.count()
                except BulkWriteError as error:
                    LOGGER.error("Bulk write issue: %s", error.details)
                    print(error.details)
                    errors_count += 1
                errors.append(errors_count)
            else:
                raise Exception("File does not exist in directory.")
        except Exception as error:
            LOGGER.error("Error: %s", error)
        finally:
            end = datetime.datetime.now()
            duration = (end - start).total_seconds()
            return (len(records[0]), record_count_before_op,
                    record_count_after_op, duration)


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
        db_id = row.pop(list(row.keys())[0])
        row['_id'] = db_id
        csv_list.append(row)
    return csv_list

def main():
    """main()
    
    Method to handle thread creation. For each file in csv,
    create a thread to import data into collection
    """
    start = datetime.datetime.now()
    print("Importing data", "start time: ", start)
    threads = []
    csvs = ['product.csv', 'customers.csv', 'rental.csv']
    for csv in csvs:
        thread = threading.Thread(target=import_data, args=('data', csv))
        LOGGER.warning(thread.getName())
        thread.start()
        threads.append(thread)
        thread.join()
    end = datetime.datetime.now()
    total_time = end - start
    print("Done importing", "end time: ", end, "\n", "total time:", total_time)

if __name__ == "__main__":
    main()
