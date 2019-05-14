import logging
import os
from peewee import *

# dynamically create a new database
# in the same directory as this script
db_folder = os.getcwd()
new_db = ("{}\customers.db".format(db_folder))


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    database = SqliteDatabase(new_db)
    database.connect()
    database.execute_sql('PRAGMA foreign_keys = ON;')

except Exception as e:
    logger.error('could not connect to database.')
    logger.error(e)


logger.info('Successfully connected to the database.')

class BaseModel(Model):
    '''
    Define base model for classes to inherit from
    '''

    class Meta:
        '''Define database (above)'''
        database = database

class Customer(BaseModel):

    cust_id = CharField(primary_key=True, max_length=30)
    cust_name = CharField(max_length=30)
    cust_last_name = CharField(max_length=30)
    cust_home_address = CharField(max_length=80)
    cust_phone = CharField(max_length=20)
    cust_email = CharField(max_length=30)
    cust_status = CharField(max_length=10) #active or inactive
    cust_credit_limit = DecimalField(decimal_places=2)


# unhash if table not yet created
database.create_tables([Customer])

database.close()
