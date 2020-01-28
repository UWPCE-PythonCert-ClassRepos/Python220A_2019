# ---------------------------------------------------------------------------- #
# Course: PYTHON 220: Advanced Programming in Python
# Script Title: Lesson 4 Assignment Peewee Data Model
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-05-25, Initial release
# ---------------------------------------------------------------------------- #

"""
    Customers data model.
"""
import os
from peewee import *


os.chdir(os.path.dirname(os.path.abspath(__file__)))
CWD = os.getcwd()

# DB_PATH = CWD + '\\customers.db'
DB_PATH = '../data/customers.db'

database = SqliteDatabase(DB_PATH)
database.connect()
database.execute_sql('PRAGMA foreign_keys = ON;')


class BaseModel(Model):
    """Model"""
    class Meta:
        """MEta"""
        database = database


class Customers(BaseModel):
    """
        This class defines customers data
    """
    customer_id = CharField(primary_key=True, max_length=30)
    name = CharField(max_length=40)
    last_name = CharField(max_length=40)
    home_address = CharField(max_length=40)
    phone_number = CharField(max_length=10)
    email_address = CharField(max_length=40)
    status = CharField(max_length=40)
    credit_limit = CharField()
