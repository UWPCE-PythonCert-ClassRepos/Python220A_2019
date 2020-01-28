# ---------------------------------------------------------------------------- #
# Course: PYTHON 220: Advanced Programming in Python
# Script Title: Lesson 3 Assignment Peewee Data Model
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-04-21, Initial release
# ---------------------------------------------------------------------------- #

"""
    Customers data model.
"""

from peewee import *
#
database = SqliteDatabase('customers.db')
database.connect()
database.execute_sql('PRAGMA foreign_keys = ON;')


class BaseModel(Model):
    class Meta:
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