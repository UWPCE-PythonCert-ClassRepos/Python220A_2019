"""
    Creates a blank DATABASE called customers.db that include s
"""
import logging
import peewee

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

DATABASE = peewee.SqliteDatabase('customers.db')
DATABASE.connect()
DATABASE.execute_sql('PRAGMA foreign_keys = ON;')


class BaseModel(peewee.Model):
    """
        Define a base model class to be inherited from.
    """
    class Meta:
        """ Defining Database """
        database = DATABASE


class Customer(BaseModel):
    """
        This class defines Customer, which maintains details of someone
        for whom we want to keep track of contact and financial info.
    """
    customer_id = peewee.IntegerField(primary_key=True)
    name = peewee.CharField(max_length=20)
    last_name = peewee.CharField(max_length=20)
    home_address = peewee.CharField(max_length=100)
    phone_number = peewee.CharField(max_length=20)
    email_address = peewee.CharField(max_length=30)
    status = peewee.CharField(max_length=10)
    credit_limit = peewee.DecimalField(decimal_places=2)

LOGGER.info('Init the DB with specified tables')
DATABASE.create_tables(
    [
        Customer
    ]
)

DATABASE.close()
