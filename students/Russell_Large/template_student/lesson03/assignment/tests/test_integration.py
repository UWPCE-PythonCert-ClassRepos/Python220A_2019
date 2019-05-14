import pytest
import sys
import os
import peewee

# dynamically connect to the database
# as long as data, src, and tests are all located
# in the same directory.
db_folder = os.getcwd()
db_location = str(db_folder[:-6] + '\src')
sys.path.append(db_location)

