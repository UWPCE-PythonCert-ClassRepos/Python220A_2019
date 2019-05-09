import csv
import logging
import pprint
import os
from pymongo import MongoClient

db_folder = os.getcwd()
print(db_folder)
loc = str(db_folder[:-4] + '\data')
product = f'{loc}\product.csv'
customer = f'{loc}\customers.csv'
rental = f'{loc}\\rental.csv'

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
    mongo = MongoDBConnection()

    with mongo:
        csvlist = [products, customers, rentals]

        for file in csvlist:
            if file == products:

                # append csv to dict list
                reader = csv.reader(open(products, 'r'))
                product_dict_list = []
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

            elif file == customers:

                # append csv to dict list
                reader = csv.reader(open(customers, 'r'))
                cust_dict_list = []
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


            elif file == rentals:

                # append csv to dict list
                reader = csv.reader(open(rentals, 'r'))
                rentals_dict_list = []
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


def show_available_products():
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
        return results_dict

def show_rentals(product_id):
    mongo = MongoDBConnection()

    with mongo:
        db = mongo.connection.HP_Norton
        rentals = db['Rentals']

        try:
            results = {}
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
                print(results)
                # pprint.pprint(info)

            return results

        except Exception as e:
            print(e)
            logger.info(f'show rentals info not successful. {e}')










# import_data('data', product, customer, rental)
# show_available_products()
# show_rentals('prd001')
