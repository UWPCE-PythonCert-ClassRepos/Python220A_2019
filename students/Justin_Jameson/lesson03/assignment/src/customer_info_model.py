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

