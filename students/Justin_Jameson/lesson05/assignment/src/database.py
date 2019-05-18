# -------------------------------------------------#
# # Title: Lesson 05 database.py
# # Dev:   Justin Jameson
# # Date:  5/18/2019
# # ChangeLog: (Who, when, What)
# -------------------------------------------------#
from pymongo import MongoClient
import sys
import csv
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ************************************** Defining variables *************************************
directory_name = '..\\.\\data\\'
product_data = 'product.csv'
customer_data = 'customers.csv'
rentals_data = 'rental.csv'
logger.info('defined directory name and the following .csv files: product_data, customer_data, and rental_data')


# ******************************************** Defining Classes *********************************
class MongoDBConnection:
    """
    MongoDB Connection
    """

    def __init__(self, host='127.0.0.1', port=27017):
        """ be sure to use the ip address not name for local windows"""
        self.host = host
        self.port = port
        self.connection = None
        logger.info('created connection to host {} and port {}'.format(self.host, self.port))

    def __enter__(self):
        self.connection = MongoClient(self.host, self.port)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


class ReadCsvFiles:
    """
    This class calls 'import_data' method to access the csv files.
    Then reads the csv files, and turns them into a list of dictionaries.
    Then sends the list to the 'main' method for incorporation into MongoDB.
    This class also uses the self items for calls in other methods.

    :return:
    """
    def __init__(self, list_of_customers=[], list_of_products=[], list_of_rentals=[]):
        self.list_of_customers = list_of_customers
        self.list_of_products = list_of_products
        self.list_of_rentals = list_of_rentals

        logger.info('created empty lists')
        imported_data = import_data(directory_name, product_data, customer_data, rentals_data)
        customers_file = imported_data[0]
        products_file = imported_data[1]
        rentals_file = imported_data[2]

        with open(customers_file, 'r') as customer:
            reader = csv.reader(customer)
            for row in reader:
                c_dict = {'User ID': row[0], 'Name': row[1], 'Address': row[2],
                          'zip code': row[3], 'phone number': row[4], 'email': row[5]}
                list_of_customers.append(c_dict)
            list_of_customers.pop(0)
        with open(products_file, 'r') as product:
            reader = csv.reader(product)
            for row in reader:
                p_dict = {'Product ID': row[0], 'Description': row[1], 'Product Type': row[2], 'Quantity available': row[3]}
                list_of_products.append(p_dict)
            list_of_products.pop(0)
        with open(rentals_file, 'r') as rentals:
            reader = csv.reader(rentals)
            for row in reader:
                r_dict = {'Product ID': row[0], 'User ID': row[1]}
                list_of_rentals.append(r_dict)
            list_of_rentals.pop(0)
        logger.info('appended all lists with content from csv files')
        return


# ************************************* user interface *************************************
def main_menu(user_prompt=None):
    """
    This method creates the menu for the program.
    """
    valid_prompts = {"1": ReadCsvFiles,
                     "2": show_available_products,
                     "3": show_rentals,
                     "4": reset_db,
                     "q": exit_program}
    options = list(valid_prompts.keys())

    while user_prompt not in valid_prompts:
        options_str = ("{}" + ", {}" * (len(options) - 1)).format(*options)
        print(f"Please choose from the following options ({options_str}):")
        print("1. Load csv files to database.")
        print("2. Show Customer products available for rent")
        print("3. Show Sales Person the list of customers")
        print("4. Reset the DataBase")
        print("q. Quit")
        user_prompt = input(">")
    return valid_prompts.get(user_prompt)


# ************************************* Processing *****************************************
def db_info():
    """
    This method returns the use of the class 'ReadCsvFiles'.
    :return:
    """
    return ReadCsvFiles()


def import_data(directory_location, product_file, customer_file, rental_file):
    """
    This function takes a directory name and three csv files as input,
    then creates a directory and file name for use in 'ReadCsvFiles' method.
           1. product data = product.csv
           2. customer data = customers.csv
           3. rentals data = rental.csv
    :param directory_location:
    :param product_file:
    :param customer_file:
    :param rental_file:
    :return:import_customer, import_product, import_rentals
    """
    import_customer = directory_location + customer_file
    import_product = directory_location + product_file
    import_rentals = directory_location + rental_file
    logger.info('returning tuple for use in method "ReadCsvFiles"')
    return import_customer, import_product, import_rentals


def main(list_of_customers, list_of_products, list_of_rentals):
    """
     Return: 2 tuples:
            1. a record count of the number of products, customers and rentals
            added (in that order)
            2. a count of any errors that occurred, in the same order.
    :param list_of_customers:
    :param list_of_products:
    :param list_of_rentals:
    :return:
    """
    mongo = MongoDBConnection()

    with mongo:  # Context manager.
        # mongodb database; create rentaldatabase
        db = mongo.connection.rentaldatabase

        # collection (table) in database, (3) customers, products and rental status (rental)
        customers = db["customers"]
        products = db["products"]
        rental = db["rental"]
        result_customer = customers.insert_many(list_of_customers)  # Inserts records specified in the list above
        result_products = products.insert_many(list_of_products)
        result_rentals = rental.insert_many(list_of_rentals)
        # print_mdb_collection(customers)  # Prints all records from a specified table
        # print_mdb_collection(products)
        # print_mdb_collection(rental)
        return result_customer, result_products, result_rentals


def reset_db():
    """
    deletes db
    :return:
    """
    mongo = MongoDBConnection()

    with mongo:  # Context manager.
        db = mongo.connection.rentaldatabase
    # start afresh next time?
    drop_data = input("Drop data?")
    if drop_data.upper() == 'Y':
        db['customers'].drop()
        db["products"].drop()
        db["rental"].drop()
        logger.info('dropped data from DB')


# ****************************************** output to the user *************************************
def show_available_products():
    """
    As a HP Norton customer I want to see a list of all products available for rent so that I can make a rental choice.
       You can have a specific field to indicate if a product is available, however,
       a quantity_available of 0 is understood as “not available”.
       Returns a Python dictionary of products listed as available with the following fields:
           product_id.
           description.
           product_type.
           quantity_available.
    :return:
    """

    for dlop in return_db_info.list_of_products:
        if dlop['Quantity available'] != '0':
            print(dlop)


def show_rentals():
    """
    Returns a Python dictionary with the following user information from users that have rented products
    matching product_id:
        user_id.
        name.
        address.
        phone_number.
        email.
    """
    for doc in return_db_info.list_of_customers:
        logger.info('producing a list of products, customers, and rentals.')
        print(doc)


# ***************************************** execution ***********************************************
def exit_program():
    """This method exits the program"""
    logger.info('called exit_program')
    sys.exit()


if __name__ == "__main__":
    return_db_info = db_info()
    while True:
        main_menu()()
        input("Press Enter to continue...........")
