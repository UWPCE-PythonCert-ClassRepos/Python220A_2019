"""
customer model
"""

import logging
from peewee import Model
from peewee import SqliteDatabase
from peewee import CharField


logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

database = SqliteDatabase('lesson04.db')
database.connect()  # if you don't say this the primary key /
# foreign key relationships won't work.  just gotta do this
database.execute_sql('PRAGMA foreign_keys = ON;')  # needed for sqlite only
LOGGER.info('Connect to database')


class BaseModel(Model):
    """
    model from peewee
    """
    class Meta:
        """
        set up db
        """
        database = database


LOGGER.info('By inheritance only we keep our model (almost) technology neutral')


class Customer(BaseModel):
    """
        This class defines Person, which maintains details of someone
        for whom we want to research career to date.
    """
    LOGGER.info('Note how we defined the class')

    LOGGER.info('Specify the fields in our model,'
                'their lengths and if mandatory')
    LOGGER.info('Must be a unique identifier for each person')
    customer_id = CharField(primary_key=True)
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=60)
    home_address = CharField(max_length=100)
    phone_number = CharField(max_length=30)
    email_address = CharField(max_length=50)
    status = CharField(max_length=20)
    credit_limit = CharField(max_length=50)
