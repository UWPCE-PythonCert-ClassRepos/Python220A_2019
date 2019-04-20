# -------------------------------------------------#
# # Title: Lesson 03 basic_operations
# # Dev:   Justin Jameson
# # Date:  4/20/2019
# # ChangeLog: (Who, when, What)
# -------------------------------------------------#
""" This file will perform interactions with the database.
Defining the database information and applying logging messages"""

import logging
from peewee import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

database = SqliteDatabase('customer_info.db')
database.connect()
database.execute_sql('PRAGMA foreign_keys = ON;')  # needed for sqlite only


def add_customer(customer_id, name, lastname, home_address, phone_number, email_address, status, credit_limit):
    """This function will add a new customer to the sqlite3 database."""
def search_customer(customer_id):
    """This function will return a dictionary object with name, lastname,
    email address and phone number of a customer or an empty dictionary object if no customer was found."""
def delete_customer(customer_id):
    """This function will delete a customer from the sqlite3 database."""
def update_customer_credit(customer_id, credit_limit):
    """This function will search an existing customer by customer_id and update their credit limit
    or raise a ValueError exception if the customer does not exist."""
def list_active_customers():
    """This function will return an integer with the number of customers whose status is currently active."""
