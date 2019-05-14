#!/usr/bin/env python3
'''
Some basic operations for the customer db
'''

import os
import logging
import peewee

class Customer(peewee.Model):
    ''' The customer model used to set up the database '''
    id = peewee.AutoField()
    name = peewee.CharField()
    lastname = peewee.CharField()
    home_address = peewee.CharField()
    phone_number = peewee.CharField()
    email = peewee.CharField()
    status = peewee.CharField()
    credit_limit = peewee.FloatField()
    class Meta:
        ''' Peewee is kinda silly and likes nested classes '''
        database = peewee.SqliteDatabase('customer.db')
        table_name = 'customers'

def setup_logger():
    ''' Sets up the db logger '''
    logger = logging.getLogger(__name__)
    log_format = " ".join(["%(asctime)s",
                           "%(filename)s:%(lineno)-3d",
                           "%(levelname)s %(message)s"])
    log_file = 'db.log'
    formatter = logging.Formatter(log_format)
    logger.setLevel(logging.DEBUG)

    file_level = logging.DEBUG
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(file_level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

def resp_to_listdict(resp):
    ''' A function to return a list of dict objects from a db response '''
    resptype = type(resp)
    if resptype == list:
        return resp
    if resptype != peewee.ModelSelect:
        return []
    data = []
    for row in resp:
        data.append(row)
    return data

def create_database():
    ''' Set up the database on disk. '''
    try:
        Customer.create_table()
    except Exception as err:
        print("Could not create database. %s", err)
        raise err

def list_active_customers():
    ''' despite the name, counts the number of active customers '''
    LOGGER.debug('Searching (listing) all active customers')
    return Customer.select().where(Customer.status == 'active').count()

def update_customer_credit(customer_id, credit_limit):
    ''' Updates the customer credit limit. '''
    LOGGER.debug('Updating customer with id %s to credit limit %s',
                 customer_id, credit_limit)
    if search_customer(customer_id):
        (Customer
         .update(credit_limit=credit_limit)
         .where(Customer.id == customer_id)
         .execute())
    else:
        raise ValueError("Could not find a customer with id %s" % customer_id)

def delete_customer(customer_id):
    ''' Deletes a customer from the db by id. '''
    LOGGER.debug('Deleting customer with id %s', customer_id)
    if Customer.delete_by_id(customer_id):
        return True
    return False

def search_customer(customer_id):
    ''' Searches for a customer by id and returns a dict '''
    LOGGER.debug('Searching for customer with id %s', customer_id)
    resp = resp_to_listdict(Customer
                            .select()
                            .where(Customer.id == customer_id)
                            .dicts())
    if resp:
        return resp[0]
    return {}

def add_customer(customer_id, name, lastname, home_address, phone_number,
                 email_address, status, credit_limit):
    ''' Adds a customer to the database.  Replaces data on conflicts '''
    LOGGER.debug('Adding customer %s %s with id %s',
                 name, lastname, customer_id)
    Customer.replace(id=customer_id, name=name, lastname=lastname,
                     home_address=home_address, phone_number=phone_number,
                     email=email_address, status=status.lower(),
                     credit_limit=credit_limit).execute()

def import_csv_data(path):
    ''' Imports csv data from a file '''

    # maps csv column headers to add_customer() args
    header_map = {'Id': 'customer_id',
                  'Name': 'name',
                  'Last_name': 'lastname',
                  'Home_address': 'home_address',
                  'Phone_number': 'phone_number',
                  'Email_address': 'email_address',
                  'Status': 'status',
                  'Credit_limit': 'credit_limit'}
    columns = []
    customers = []
    try:
        with open(path, encoding="ISO-8859-1") as fhand:
            # retrieve the csv header and map it to add_customer args
            header = fhand.readline().rstrip()
            cols = header.split(',')
            for col in cols:
                columns.append(header_map[col])

            # retrieve each row and populate customers[]
            for line in fhand:
                fields = line.rstrip().split(',')
                customer = {}
                for field in enumerate(fields):
                    # cook customer_id
                    if columns[field[0]] == 'customer_id':
                        customer[columns[field[0]]] = int(field[1][1:])
                    else:
                        customer[columns[field[0]]] = field[1]
                customers.append(customer)
    except Exception as err:
        LOGGER.error('Failure to read data from %s: %s', path, err)
        raise err

    try:
        for customer in customers:
            add_customer(**customer)
    except Exception as err:
        LOGGER.error('Failure to add customer %s to db: %s', path, err)
        raise err

# The homework doc said we need to create a default db called customer.db
create_database()

LOGGER = logging
if __name__ == "__main__":
    LOGGER = setup_logger()

    # get the real path of this script
    SRC_PATH = os.path.realpath(__file__)

    # assuming data is in ../data/customer.csv relative to above
    DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(SRC_PATH)),
                             "data/customer.csv")

    import_csv_data(DATA_PATH)
