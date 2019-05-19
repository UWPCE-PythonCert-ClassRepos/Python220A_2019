"""
# Title: basic_operations.py
# Desc: Establishes the basic operations for
# Assignment04
# Change Log: (Who, When, What)
# KCreek, 4/24/2019, Created Script
"""

# Revision: Changed import statements
from customer_model import *
import peewee
import logging


def set_up_logger():
    # Create Default to set Logging Level
    """
    Function to set up logger for debug and errors
    :return: None
    """
    # Change Debugger Level to an Integer
    # Set Log Formatting Options
    log_format = "%(asctime)s %(filename)s:%(lineno)-4d %(levelname)s %(message)s"

    # Create formatter object
    formatter = logging.Formatter(log_format)

    # Set Log File Locations
    file_handler = logging.FileHandler('db.log')

    # Pass Formatter to file handler
    file_handler.setFormatter(formatter)

    # Create an instance of the Logger
    logger = logging.getLogger()
    # Pass File Handler to the logger
    logger.addHandler(file_handler)

    # Set minimum Logging Level
    logger.setLevel(logging.INFO)

    # Remove Stream Handler
    logger.removeHandler(logging.StreamHandler)


# Added code for Existence of Table
def table_check(table_name=None):
    """
    Function Checks to ensure Customer Table exists in
    customers.db. Creates table if it does not exist.
    :return: None
    """
    set_up_logger()

    if table_name is None:
        logging.warning("No table_name provided to Check!")
    else:
        table_list = database.get_tables()

        if table_name not in table_list:
            database.create_tables([Customer])
            logging.info("Customer Table Created in lesson04.db")
        else:
            logging.info("Customer Table already exists!")


def search_customer(customer_id):
    """
    Returns a dictionary of Customer w/ Desired
    Customer ID
    :param customer_id: Customers ID
    :return: Dictionary of  Customer
    """
    set_up_logger()

    try:
        # Query Customer Database for row
        data = Customer.get(Customer.customer_id == customer_id)
        # Place Data into a return dictionary
        return_dict = {"customer_id":data.customer_id,
                       "first_name": data.first_name,
                       "last_name": data.last_name,
                       "email_address": data.email_address,
                       "phone_number": data.phone_number,
                       "credit_limit":data.credit_limit
                       }
        logging.info("The Following Dictionary was created: {}".format(return_dict))
        return return_dict
    # Exception where query target does not exist
    except Exception as e:
        logging.warning("The Following Exception Occurred: {}".format(e))
        return {}


def add_customer(customer_id=None, first_name=None, last_name=None,
                 home_address=None, phone_number=None,
                 email_address=None, status=None, credit_limit=None):
    """
    Adds Customers to the sqlite3 Database 'Customer.db'
    :param customer_id: Customer ID Number (int)
    :param first_name: Customer First Name (str)
    :param last_name: Customer Last Name
    :param home_address: Customer Home Address
    :param phone_number: Customer Phone Number
    :param email_address: Customer email Address
    :param status: Customer Status
    :param credit_limit: Customer Credit limit
    :return: None. Customer is added to Database
    """
    set_up_logger()

    check_list = [customer_id, first_name, last_name, home_address,
                  email_address, status, credit_limit]
    # Potential to re-factor code here
    for parameter in check_list:
        if parameter is None:
            logging.info("{} was entered as 'None' when adding customer".format(parameter))
            pass
    # Establish connection w/ Database
    try:
        with database.transaction():
            # Provide fields required for new_customer
            new_customer = Customer.create(
                customer_id=customer_id,
                first_name=first_name,
                last_name=last_name,
                home_address=home_address,
                phone_number=phone_number,
                email_address=email_address,
                status=status,
                credit_limit=credit_limit
            )
            new_customer.save()
            logging.info("New Customer {} Added!".format(customer_id))
    # Error Handling accounts for duplicate Customer ID's are Unique in DB
    except peewee.IntegrityError:
        pass
        logging.warning("Customer {} Not Created, CustomerID {} is taken"\
                     .format(first_name, customer_id))


def delete_customer(customer_id):
    """
    Deletes a customer from Customer Database
    :param customer_id: Customers ID
    :return: None.
    """

    set_up_logger()
    try:
        cust = Customer.get(Customer.customer_id == customer_id)
        cust.delete_instance()
        logging.info("Customer {} Successfully Deleted!".format(customer_id))

    except Exception as e:
        logging.warning("The Following Delete Exception Occurred: {}".format(e))


def update_customer_credit(customer_id, credit_limit):
    """
    Searches for an existing Customer by customer_id and
    updates customer's credit limit.
    :param customer_id: Customer's ID
    :param credit_limit: Customers Credit Limit
    :return: None
    """
    set_up_logger()

    try:
        Customer.update(credit_limit=credit_limit)\
            .where(Customer.customer_id == customer_id).execute()

        logging.info("Customer {} Credit Limit Updated to {}".format(\
            customer_id, credit_limit))

    except Exception as e:
        logging.warning("The following Update Exception Occurred: {}".format(e))


def list_active_customers():
    """
    Returns an integer with the number of customers whose
    status is currently active
    :return: Integer of active customers
    """

    set_up_logger()
    counter = 0
    # potential to re-factor code here
    for customer in Customer.select():
        if customer.status == 'active':
            counter += 1
    logging.info("Number of Active Customers: {}".format(counter))
    return counter

