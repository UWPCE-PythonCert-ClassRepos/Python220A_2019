import peewee
from basic_operations import add_customer
from basic_operations import search_customer

# Create and connect to a database
db = peewee.SqliteDatabase(":memory:")
db.connect()
db.execute_sql('PRAGMA foreign_keys = ON;') # needed for sqlite only

# Create the Base Model Class
class BaseModel(peewee.Model):
    """
    Established the Base Model Class. Inhereting from
    Pee Wee Model Class
    """

    class Meta:
        """"
        Defines the Class Meta-Data and defines
        database
        """

        database = db


# Establish the Customer Class
class Customer(BaseModel):
    """
    This class Defines the customer class to maintain customer
    information
    """
    def __init__(self, db_file):
        db.init(db_file)

    customer_id = peewee.CharField(primary_key=True, max_length=30)
    first_name = peewee.TextField()
    last_name = peewee.TextField()
    home_address = peewee.TextField()
    phone_number = peewee.CharField(max_length=12)
    email_address = peewee.TextField()
    status = peewee.TextField()
    credit_limit = peewee.IntegerField()


# Create a table in the database which exists in memory
database.create_tables([Customer])

# Add a Customer
customer1 = [1, 'Kyle', 'Creek', '11550 6th Pl NE', '253-315-3049', 'kyle.a.creek@gmail.com', 'active', 750]
add_customer(*customer1)

# Get the dicitonary of the customer
d = search_customer(1)
print(d)