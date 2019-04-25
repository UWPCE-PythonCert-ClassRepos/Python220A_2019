from peewee import *
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info('Here we define our data (the schema)')
logger.info('First name and connect to a database (sqlite here)')

logger.info('The next 3 lines of code are the only database specific code')

database = SqliteDatabase('lesson03.db')
database.connect()  # if you don't say this the primary key / foreign key relationships won't work.  just gotta do this
database.execute_sql('PRAGMA foreign_keys = ON;')  # needed for sqlite only
logger.info('Connect to database')


class BaseModel(Model):
    class Meta:
        database = database


logger.info('By inheritance only we keep our model (almost) technology neutral')


class Customer (BaseModel):
    """
        This class defines Person, which maintains details of someone
        for whom we want to research career to date.
    """
    logger.info('Note how we defined the class')

    logger.info('Specify the fields in our model, their lengths and if mandatory')
    logger.info('Must be a unique identifier for each person')
    customer_id = IntegerField(primary_key=True)
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=40)
    home_address = CharField(max_length=100)
    phone_number = IntegerField()
    email_address = CharField(max_length=50)
    status = BooleanField()
    credit_limit = IntegerField()
