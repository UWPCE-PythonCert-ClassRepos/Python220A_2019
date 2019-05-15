from pymongo import MongoClient
import csv


class MongoDBConnection:
    """MongoDB Connection"""

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


def print_mdb_collection(collection_name):
    for doc in collection_name.find():
        print(doc)


def read_csv_files():
    list_of_customers = []
    list_of_products = []
    list_of_rentals = []
    with open('..\\.\\data\\customers.csv', 'r') as customer:
        reader = csv.reader(customer)
        for row in reader:
            c_dict = {'User ID': row[0], 'Name': row[1], 'Address': row[2],
                      'zip code': row[3], 'phone number': row[4], 'email': row[5]}
            list_of_customers.append(c_dict)
        list_of_customers.pop(0)
    with open('..\\.\\data\\product.csv', 'r') as product:
        reader = csv.reader(product)
        for row in reader:
            p_dict = {'Product ID': row[0], 'Description': row[1], 'Product Type': row[2], 'Quantity available': row[3]}
            list_of_products.append(p_dict)
        list_of_products.pop(0)
    with open('..\\.\\data\\rental.csv', 'r') as rentals:
        reader = csv.reader(rentals)
        for row in reader:
            r_dict = {'Product ID': row[0], 'User ID': row[1]}
            list_of_rentals.append(r_dict)
        list_of_rentals.pop(0)
    main(list_of_customers, list_of_products, list_of_rentals)


def main(list_of_customers, list_of_products, list_of_rentals):
    mongo = MongoDBConnection()

    with mongo:  # Context manager.
        # mongodb database; create rentaldatabase
        db = mongo.connection.rentaldatabase

        # collection (table) in database, (3) customers, products and rental status (rental)
        customers = db["customers"]  # todo: if the db is failing, review original code from instructor for syntax
        # todo: create method to define the list of dictionaries for customers, pass in as an argument
        products = db["products"]
        rental = db["rental"]
        result_customer = customers.insert_many(list_of_customers)  # Inserts records specified in the list above
        result_products = products.insert_many(list_of_products)
        result_rentals = rental.insert_many(list_of_rentals)
        print_mdb_collection(customers)  # Prints all records from a specified table
        print_mdb_collection(products)
        print_mdb_collection(rental)

        """ # related data
        for CurrentRecord in ThePersonWhoCollects.find():  # Here CurrentRecord is a variable 
        pointing to each found record in a table
            # CurrentRecord is a dictionary (EACH record is a dictionary). We can refer an element of the dictionary
            # by its key; one of the keys is called "name"
            print(customer'List for {CurrentRecord["name"]}')
            query = {"name": CurrentRecord["name"]}
            for a_cd in cd.find(
                    query):  # Find all the records from table "cd" where attribute name 
                    is equal to a specified value (which happens to be a
                # a name of a current record). In general, keys from records need satisfy properties specified in query
                print(customer'{CurrentRecord["name"]} has collected {a_cd}')
        """
        # start afresh next time?
        yorn = input("Drop data?")
        if yorn.upper() == 'Y':
            customers.drop()
            products.drop()
            rental.drop()  # Deletes the table and the data


if __name__ == "__main__":
    read_csv_files()
