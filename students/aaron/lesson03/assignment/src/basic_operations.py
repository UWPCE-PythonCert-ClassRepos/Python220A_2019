'''
Some basic operations for the customer db
'''

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
        print("Could not create database. %s" % err)
        raise err

def list_active_customers():
    ''' despite the name, counts the number of active customers '''
    return Customer.select().where(Customer.status == 'active').count()

def update_customer_credit(customer_id, credit_limit):
    ''' Updates the customer credit limit. '''
    if search_customer(customer_id):
        (Customer
         .update(credit_limit=credit_limit)
         .where(Customer.id == customer_id)
         .execute())
    else:
        raise ValueError("Could not find a customer with id %s" % customer_id)

def delete_customer(customer_id):
    ''' Deletes a customer from the db by id. '''
    if Customer.delete_by_id(customer_id):
        return True
    return False

def search_customer(customer_id):
    ''' Searches for a customer by id and returns a dict '''
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
    Customer.replace(id=customer_id, name=name, lastname=lastname,
                     home_address=home_address, phone_number=phone_number,
                     email=email_address, status=status.lower(),
                     credit_limit=credit_limit).execute()

# The homework doc said we need to create a default db called customer.db
create_database()
