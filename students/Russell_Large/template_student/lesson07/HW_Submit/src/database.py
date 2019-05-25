import csv
import logging
import pprint
import os
import time
from pymongo import MongoClient
from multiprocessing import Process

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MongoDBConnection():
    """MongoDB Connection. automatically connects to the db. will automatically close the db. """

    def __init__(self, host='127.0.0.1', port=27017):
        """ be sure to use the ip address not name for local windows"""
        self.host = host
        self.port = port
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient(self.host, self.port)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


def create_collection(dataset, db, dict_list):

    collection = db[dataset]

    #retrive inital record count
    initial_count = collection.count()

    # take all records out (testing, remove for production)
    collection.drop()

    # insert data to collection, get count
    result = collection.insert_many(dict_list)
    inserted_count = len(result.inserted_ids)

    # total count of records
    total_count = collection.count()

    # print(f'the total number of {dataset} records before: {t}')

    return initial_count, inserted_count, total_count

def import_data(dir, dataset):

    product_dict_list = []
    cust_dict_list = []
    errors = []
    filelocation = r'{}\\{}.csv'.format(dir, dataset)

    # 1. # of records processed (int)
    # 2. record count in the database prior to running (int)
    # 3. record count after running (int)
    # 4. time taken to run the module (float)

    cust_init_count = []
    cust_inserted_count = []
    cust_total_records = []
    cust_time = []

    product_init_count = []
    product_inserted_count = []
    product_total_records = []
    product_time = []


    mongo = MongoDBConnection()

    with mongo:

        db = mongo.connection.HP_Norton

        if dataset == 'product':
            beginning_time = time.time()
            reader = csv.reader(open(filelocation, 'r'))
            errors_count = 0

            try:
                for row in reader:
                    dict = ({
                            '_id': row[0],
                            'description': row[1],
                            'product_type': row[2],
                            'quantity_available': row[3],
                            })
                    product_dict_list.append(dict)

                do_it = create_collection(dataset, db, product_dict_list)

                product_init_count.append(do_it[0])
                product_inserted_count.append(do_it[1])
                product_total_records.append(do_it[2])

                elapsed_time = time.time() - beginning_time

                # logger.info(f'{pprint.pprint(cust_dict_list)}')
                logger.info(f'Total {dataset} initial records: {do_it[0]}. \n'
                            f'Total {dataset} inserted records: {do_it[1]}. \n'
                            f'Total {dataset} records in collection: {do_it[2]}. \n'
                            f'Total {dataset} data runtime: {elapsed_time}')

            except Exception as e:
                logger.error('Error occured adding product data to db.')
                logger.error(e)
                errors_count += 1
                errors.append('product errors:' + str(errors_count))


        elif dataset == 'customer':
            beginning_time = time.time()
            errors_count = 0
            filelocation = r'{}\\{}.csv'.format(dir, dataset)
            # print(filelocation)
            reader = csv.reader(open(filelocation, 'r'))
            # header = next(reader)
            try:
                for row in reader:
                    dict = ({'_id': row[0],
                             'cust_name': row[1],
                             'cust_address': row[2],
                             'cust_zip': row[3],
                             'cust_phone': row[4],
                             'cust_email': row[5]
                             })
                    cust_dict_list.append(dict)

                do_it = create_collection(dataset, db, cust_dict_list)

                cust_init_count.append(do_it[0])
                cust_inserted_count.append(do_it[1])
                cust_total_records.append(do_it[2])


                elapsed_time = time.time() - beginning_time
                cust_time.append(float(elapsed_time))

                # logger.info(f'{pprint.pprint(cust_dict_list)}')
                logger.info(f'Total {dataset} initial records: {do_it[0]}. \n'
                            f'Total {dataset} inserted records: {do_it[1]}. \n'
                            f'Total {dataset} records in collection: {do_it[2]}. \n'
                            f'Total {dataset} data runtime: {elapsed_time}')

            except Exception as e:
                logger.info('Error occured adding customer data to db.')
                logger.info(e)
                errors_count += 1
                errors.append('customer errors:' + str(errors_count))

    cust_tuple = [cust_init_count, cust_inserted_count,
                  cust_total_records, cust_time]
    product_tuple = [product_init_count, product_inserted_count,
                     product_total_records, product_time]

    return cust_tuple, product_tuple


