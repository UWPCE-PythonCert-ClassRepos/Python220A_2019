# -------------------------------------------------#
# # Title: Lesson 03 customer_class
# # Dev:   Justin Jameson
# # Date:  4/20/2019
# # ChangeLog: (Who, when, What)
# -------------------------------------------------#
"""Defining the database information and applying logging messages"""

import logging
from peewee import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

database = SqliteDatabase('customer_info.db')
database.connect()
database.execute_sql('PRAGMA foreign_keys = ON;') # needed for sqlite only


class BaseModel(Model):
    class Meta:
        database = database


class Customer(BaseModel):
    """
        This class defines the Customer attribute information for the table 'Customer'.
    """
    customer_id = CharField(primary_key=True, max_length=10)
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)
    home_address = CharField(max_length=30)
    phone_number = CharField(max_length=15, null=True)
    email_address = CharField(max_length=30)
    customer_status = CharField(max_length=30)
    credit_limit = DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        database = database  # using 'customer_info.db'


def create_table():
    database.create_tables([Customer])


def delete_customer(customer_id):
    customer_id.deleteinstance()

# create_table()
