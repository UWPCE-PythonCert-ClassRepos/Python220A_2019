# ---------------------------------------------------------------------------- #
# Course: PYTHON 220: Advanced Programming in Python
# Script Title: Lesson 3 Assignment
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-04-21, Initial release
# ---------------------------------------------------------------------------- #
"""
Basic relational database operations for inventory system
"""
import logging
import csv
from data_model import Customers

LOG_FORMAT = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s " \
             "%(message)s"
LOG_LEVEL = 'DEBUG'

logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)
console_handler = logging.StreamHandler()
console_handler.setLevel(LOG_LEVEL)
formatter = logging.Formatter(LOG_FORMAT)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


def create_table():
    """
    Create DB table
    """
    try:
        database.create_tables([Customers])
        logger.debug('Creating "Customers" database table...')

    except Exception as error:
        # logger.info('Database Table exists')
        logger.debug('Database table exists. Error: {}'.format(error))


def read_data_file():
    """
    Read customer data from csv file and populate DB table
    """

    with open('customer.csv') as csvfile:
        customer_data = csv.reader(csvfile, delimiter=',')

        # try:
        for customer in customer_data:
            try:
                with database.transaction():
                    new_customer = Customers.create(
                        customer_id=customer[0],
                        name=customer[1],
                        last_name=customer[2],
                        home_address=customer[3],
                        phone_number=customer[4],
                        email_address=customer[5],
                        status=customer[6],
                        credit_limit=customer[7]
                    )
                    new_customer.save()
                    logger.debug('Adding Customer with ID = {}'
                                 .format(customer[0]))

            except Exception as error:
                logger.debug('Customer ID {} already in Database. Error: {}'
                             .format(customer[0], error))


def add_customer(customer_id, name, last_name, home_address, phone_number,
                 email_address, status, credit_limit):
    """
    Add new customer to DB table
    """
    try:
        with database.transaction():
            new_customer = Customers.create(
                customer_id=customer_id,
                name=name,
                last_name=last_name,
                home_address=home_address,
                phone_number=phone_number,
                email_address=email_address,
                status=status,
                credit_limit=credit_limit
            )
            new_customer.save()
            logger.debug('Saving Customer with ID = {}'.format(customer_id))
    except Exception as error:
        logger.debug('Customer ID {} already in Database. Error: {}'
                     .format(customer_id, error))


def search_customer(customer_id):
    """
    Search customer by Customer ID
    :param customer_id:
    :return:
    """
    try:
        with database.transaction():
            customer = Customers.get(Customers.customer_id == customer_id)

            logger.debug('Searching for Customer with ID = {}'
                         .format(customer.customer_id))

            logger.debug('Customer found: Full Name: {}, {}'
                         .format(customer.last_name, customer.name))

            return (customer.customer_id, customer.name, customer.last_name,
                    customer.home_address, customer.phone_number,
                    customer.email_address, customer.status,
                    customer.credit_limit)
    except Exception as error:
        logger.debug('Customer ID = {} not found. Error: {}'
                     .format(customer_id, error))
        # logger.info(e)
        return {}


def delete_customer(customer_id):
    """
    Delete customer by customer ID
    :param customer_id:
    :return:
    """
    logger.debug('Delete customer ID = {}'.format(customer_id))
    try:
        with database.transaction():
            customer = Customers.get(Customers.customer_id == customer_id)
            logger.debug('Deleting Customer ID = {}...'
                         .format(customer_id))
            customer.delete_instance()
            return True

    except Exception as error:
        logger.debug('Error {}'.format(error))


def update_customer_credit(customer_id, new_credit_limit):
    """Update customer credit limit"""
    logger.debug('Updating credit limit for Customer ID: {}'
                 .format(customer_id))

    try:
        customer = Customers.get(Customers.customer_id == customer_id)

        logger.debug('Existing Values: Customer ID: {}, Credit Limit: {}'
                     .format(customer.customer_id, customer.credit_limit))

        customer.credit_limit = new_credit_limit

        customer.save()

    except Exception as error:
        logger.debug('Customer ID = {} not found. Error: {}'
                     .format(customer_id, error))


def list_active_customers():
    """Count active customers"""
    try:
        logger.debug('Searching active customers...')

        # active_list = Customers.select().where(Customers.status == 'active')
        active_count = Customers \
            .select() \
            .where(Customers.status == 'Active') \
            .count()

        return active_count

    except Exception as error:
        logger.debug('No Active customers found. Error: {}'
                     .format(error))


if __name__ == '__main__':
    create_table()

    read_data_file()
