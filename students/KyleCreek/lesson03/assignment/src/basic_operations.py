"""
# Title: basic_operations.py
# Desc: Establishes the basic operations for
# Assignment03
# Change Log: (Who, When, What)
# KCreek, 4/20/2019, Created Script
"""

#from assignment.src.customer_model import *
from assignment.src.customer_model import *
import peewee
import logging


def search_customer(customer_id):
    """
    Returns a dictionary of Customer w/ Desired
    Customer ID
    :param customer_id: Customers ID
    :return: Dictionary of  Customer
    """
    try:
        # Query Customer Database for row
        data = Customer.get(Customer.customer_id == customer_id)
        # Place Data into a return dictionary
        return_dict = {"First Name": data.first_name, "Last Name": data.last_name,
                       "Email": data.email_address,"Phone Number": data.phone_number}
        logging.info("The Following Dictionary was created: {}".format(return_dict))
        return return_dict
    # Exception where query target does not exist
    except Exception as e:
        logging.info("The Following Exception Occured: {}".format(e))
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

    check_list = [customer_id, first_name, last_name, home_address,
                  email_address, status, credit_limit]

    for parameter in check_list:
        if parameter is None:
            logging.info("{} was entered as 'None' when adding customer".format(parameter))
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
    except peewee.IntegrityError:
        logging.info("Customer {} Not Created, CustomerID {} is taken"\
                     .format(first_name, customer_id))


def delete_customer(customer_id):
    """
    Deletes a customer from Customer Database
    :param customer_id: Customers ID
    :return: None.
    """
    try:
        cust = Customer.get(Customer.customer_id == customer_id)
        cust.delete_instance()
        logging.info("Customer {} Successfully Deleted!".format(customer_id))

    except Exception as e:
        logging.info("The Following Delete Exception Occurred: {}".format(e))


def update_customer_credit(customer_id, credit_limit):
    """
    Searches for an existing Customer by customer_id and
    updates customer's credit limit.
    :param customer_id: Customer's ID
    :param credit_limit: Customers Credit Limit
    :return: None
    """
    try:
        Customer.update(credit_limit=credit_limit)\
            .where(Customer.customer_id == customer_id).execute()

        logging.info("Customer {} Credit Limit Updated to {}".format(\
            customer_id, credit_limit))

    except Exception as e:
        logging.info("The following Update Exception Occurred: {}".format(e))


def list_active_customers():
    """
    Returns an integer with the number of customers whose
    status is currently active
    :return: Integer of active customers
    """
    counter = 0
    for customer in Customer.select():
        if customer.status == 'active':
            counter += 1
    logging.info("Number of Active Customers: {}".format(counter))
    return counter

cust1 = add_customer(1, "first", "last", "address", "phone", "email", "status", 700)