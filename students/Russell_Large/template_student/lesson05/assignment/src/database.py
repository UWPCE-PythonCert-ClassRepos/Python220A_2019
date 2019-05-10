import csv
import logging
import pprint
import os
from pymongo import MongoClient

# # add into import
# db_folder = os.getcwd()
# # print(db_folder)
# loc = str(db_folder[:-4] + '\data')
# product = f'{loc}\product.csv'
# customer = f'{loc}\customers.csv'
# rental = f'{loc}\\rental.csv'

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


def import_data(dir, products, customers, rentals):
    '''
    Import different types of CSV data into MongoDB.
    :param dir: 
    :param products: 
    :param customers: 
    :param rentals: 
    :return: 
    '''
    mongo = MongoDBConnection()

    with mongo:
        csvlist = [products, customers, rentals]
        product_dict_list = []
        cust_dict_list = []
        rentals_dict_list = []
        errors = []
        for file in csvlist:
            if file == products:
                errors_count = 0
                # append csv to dict list
                reader = csv.reader(open(products, 'r'))

                try:
                    for row in reader:
                        product_dict = ({
                                '_id': row[0],
                                'description': row[1],
                                'product_type': row[2],
                                'quantity_available': row[3],
                                })
                        product_dict_list.append(product_dict)

                    # connect to mongodb, create collection
                    db = mongo.connection.HP_Norton
                    collection = db['Products']
                    collection.drop()

                    # insert data to 'Products' collection
                    result = collection.insert_many(product_dict_list)

                    # produce count from input
                    count = len(result.inserted_ids)
                    #logger.info(f'test{pprint.pprint(product_dict_list)}')
                    logger.info(f'Total Product records added: {count}')
                    # print(f'Total records added: {count}')
                except Exception as e:
                    logger.info('Error occured adding data to db.')
                    logger.info(e)
                    errors_count += 1
                    errors.append('product errors:' + str(errors_count))

            #provide record count of number of items
            # provide count of any errors that occured, in the same order

            elif file == customers:
                errors_count = 0
                # append csv to dict list
                reader = csv.reader(open(customers, 'r'))
                try:
                    for row in reader:
                        cust_dict = ({'_id': row[0],
                                 'cust_name': row[1],
                                 'cust_address': row[2],
                                 'cust_zip': row[3],
                                 'cust_phone': row[4],
                                 'cust_email': row[5]
                                 })
                        cust_dict_list.append(cust_dict)

                    # connect to mongodb, create collection
                    db = mongo.connection.HP_Norton
                    collection = db['Customer']
                    collection.drop()

                    # insert data to 'Products' collection
                    result = collection.insert_many(cust_dict_list)

                    # produce count from input
                    count = len(result.inserted_ids)
                    #logger.info(f'{pprint.pprint(cust_dict_list)}')
                    logger.info(f'Total Customer records added: {count}')
                    # print(f'Total records added: {count}')
                except Exception as e:
                    logger.info('Error occured adding data to db.')
                    logger.info(e)
                    errors_count += 1
                    errors.append('customer errors:' + str(errors_count))


            elif file == rentals:
                errors_count = 0
                reader = csv.reader(open(rentals, 'r'))
                try:
                    # append csv to dict list
                    for row in reader:
                        rentals_dict = ({'product_id': row[0],
                                        'user_id': row[1]
                                        })
                        rentals_dict_list.append(rentals_dict)

                    # connect to mongodb, create collection
                    db = mongo.connection.HP_Norton
                    collection = db['Rentals']
                    collection.drop()

                    # insert data to 'Products' collection
                    result = collection.insert_many(rentals_dict_list)

                    # produce count from input
                    count = len(result.inserted_ids)
                    #logger.info(f'{pprint.pprint(rentals_dict_list)}')
                    logger.info(f'Total Rentals records added: {count}')
                    # print(f'Total records added: {count}')

                except Exception as e:
                    logger.info('Error occured adding data to db.')
                    logger.info(e)
                    errors_count += 1
                    errors.append('customer errors:' + str(errors_count))

        all_results = (product_dict_list, cust_dict_list, rentals_dict_list)
        return tuple(all_results), tuple(errors)

def show_available_products():
    '''
    Query function returns all Product collection data that has a 
    'quantity_available' greater than 0. Also returns a 'test'
    variable that helps with testing. 
    :return: 
    '''
    mongo = MongoDBConnection()

    with mongo:
        db = mongo.connection.HP_Norton
        collection = db['Products']

        results_dict = {}

        for avail in collection.find({"quantity_available": {'$gt': '0'}}):
            id = avail.pop('_id')
            products = avail['description']
            results_dict[id] = avail
            logger.info(f'Products available: {products}')

        test = tuple(results_dict.keys())

        return results_dict, test

def show_rentals(product_id):
    '''
    Query function that matches rentals collection data with customer collection
    data from the rentals collection. query will return data that matches. 
    :param product_id: 
    :return: 
    '''
    mongo = MongoDBConnection()
    results = {}

    with mongo:
        db = mongo.connection.HP_Norton
        rentals = db['Rentals']

        try:

            for info in rentals.aggregate([
                {
                    '$lookup':
                        {
                            'from': 'Customer',
                            'localField': 'user_id', #common field from Rentals
                            'foreignField': '_id', # common field from Customer
                            'as': 'ID' # alias name for Customer
                        }
                },
                            {'$match': {'product_id': product_id}}]):
                results['Rentals'] = info

        except Exception as e:
            print(e)
            logger.info(f'show rentals info not successful. {e}')

    test = f"{results.keys()}"

    return results, test
