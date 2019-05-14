"""
# Title: customer_model.py
# Desc: Establishes the Customer Model
# Change Log: (Who, When, What)
# KCreek, 4/18/2019, Created Script
"""

from peewee import *
import logging

# Create a logger to log actions
logging.basicConfig(level=logging.INFO)

# Create a database and Connect
database = SqliteDatabase('lesson04.db')
database.connect()
logging.info("Connected to Database lesson04")
database.execute_sql('PRAGMA foreign_keys = ON;')


# Create the Base Model Class
class BaseModel(Model):
    """
    Established the Base Model Class. Inhereting from
    Pee Wee Model Class
    """

    class Meta:
        """"
        Defines the Class Meta-Data and defines
        database
        """

        database = database


# Establish the Customer Class
class Customer(BaseModel):
    """
    This class Defines the customer class to maintain customer
    information
    """

    customer_id = CharField(primary_key=True, max_length=30)
    first_name = TextField()
    last_name = TextField()
    home_address = TextField()
    phone_number = CharField(max_length=12)
    email_address = TextField()
    status = TextField()
    credit_limit = IntegerField()

