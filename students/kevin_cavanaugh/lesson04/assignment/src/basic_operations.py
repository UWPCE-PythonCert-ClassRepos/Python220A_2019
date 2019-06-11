"""
Operations class to create, remove, update, and delete customer data
"""

import logging
import csv
from datetime import datetime
from peewee import IntegrityError
from peewee import DoesNotExist
from peewee import fn
from customer_model import database
from customer_model import Customer


# set up format of logging outputs & log file name
LOG_FORMAT = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
LOG_FILE = datetime.now().strftime("%Y-%m-%d") + '_db.log'
FORMATTER = logging.Formatter(LOG_FORMAT)

# set up logger
LOGGER = logging.getLogger(__name__)

# set up file
FILE_HANDLER = logging.FileHandler(LOG_FILE)
FILE_HANDLER.setFormatter(FORMATTER)
FILE_HANDLER.setLevel(logging.INFO)
LOGGER.addHandler(FILE_HANDLER)

# set up console
CONSOLE_HANDLER = logging.StreamHandler()
CONSOLE_HANDLER.setFormatter(FORMATTER)
CONSOLE_HANDLER.setLevel(logging.ERROR)
LOGGER.addHandler(CONSOLE_HANDLER)

#  customer attributes (column names)
CUSTOMER_ID = 0
FIRST_NAME = 1
LAST_NAME = 2
HOME_ADDRESS = 3
PHONE_NUMBER = 4
EMAIL_ADDRESS = 5
STATUS = 6
CREDIT_LIMIT = 7


def add_customer(cust_id, f_name, l_name, addr, phone, email, status, limit):
    """
    add new customer to table
    """
    try:

        LOGGER.info("Create Customer record")

        with database.transaction():

            new_customer = Customer.create(
                customer_id=cust_id,
                first_name=f_name,
                last_name=l_name,
                home_address=addr,
                phone_number=phone,
                email_address=email,
                status=status,
                credit_limit=limit
            )
            new_customer.save()
            LOGGER.info('Successfully added new customer: %s',
                        new_customer.custmer_id)
            LOGGER.info('id: %s', new_customer.customer_id)
            LOGGER.info('first: %s', new_customer.first_name)
            LOGGER.info('last: %s', new_customer.first_name)
            LOGGER.info('address: %s', new_customer.home_address)
            LOGGER.info('phone: %s', new_customer.phone_number)
            LOGGER.info('email: %s', new_customer.email_address)
            LOGGER.info('status: %s', new_customer.status)
            LOGGER.info('limit: %s', new_customer.credit_limit)

    except IntegrityError as err:

        LOGGER.warning('Error creating customer: %s', cust_id)
        LOGGER.warning(err)

    return Customer


def search_customer(customer_id):
    """
    search & return customer dict based on id
    """
    try:
        customer = Customer.get(Customer.customer_id == customer_id)
        LOGGER.info('searching for customer %s', customer.customer_id)

        results = {
            'first_name': customer.first_name,
            'last_name': customer.last_name,
            'email_address': customer.email_address,
            'phone_number': customer.phone_number
        }
        LOGGER.info(results)
    except DoesNotExist as err:
        LOGGER.warning('customer ID: %s , not found', customer_id)
        LOGGER.warning(err)
        results = {}
    return results


def delete_customer(customer_id):
    """
    delete customer based on customer id
    :return:
    """
    try:
        customer = Customer.get(Customer.customer_id == customer_id)
        LOGGER.info('User wishes to delete: %s', customer)
        customer.delete_instance()
        LOGGER.info('Successfully deleting: %s', customer)

        return True

    except DoesNotExist as err:

        LOGGER.warning('Error deleting customer: %s', customer_id)
        LOGGER.warning(err)

    return False


def update_customer(customer_id, credit_limit):
    """
    update customer limit based on user id
    :return:
    """
    try:
        with database.transaction():
            customer_update = Customer.get(Customer.customer_id == customer_id)
            LOGGER.info('limit before update: %s',
                        customer_update.credit_limit)
            customer_update.credit_limit = credit_limit
            LOGGER.info('limit post update: %s', customer_update.credit_limit)

        return True

    except DoesNotExist as err:

        LOGGER.warning('Error updating customer: %s', customer_id)
        LOGGER.warning(err)

    return False


def list_active_customers():
    """
    return active user count
    """
    with database.transaction():
        query = (Customer
                 .select(fn.COUNT(Customer.status).alias('count'))
                 .where(Customer.status == 'Active'))
        LOGGER.info(query)

    customer_count = [item.count for item in query]
    LOGGER.info('number of active customers %s', customer_count[0])
    return customer_count[0]


def data_from_csv(csv_file):
    """
    read data from csv & return list to import into bd
    :param csv_file
    """
    with open(csv_file, encoding='utf-8', errors='ignore') as people:
        customer_reader = csv.reader(people)
        customers = [n for n in customer_reader]

    return customers


if __name__ == '__main__':

    DATA = data_from_csv(r'C:\Python220\Python220A_2019\students'
                         r'\kevin_cavanaugh\Lesson03\assignment'
                         r'\data\customer.csv')

    database.create_tables([Customer])
    logging.info('Created table: %s', Customer.__name__)

    # #  add customers
    # for customer in DATA[1:]:
    #     add_customer(customer[CUSTOMER_ID],
    #                  customer[FIRST_NAME],
    #                  customer[LAST_NAME],
    #                  customer[HOME_ADDRESS],
    #                  customer[PHONE_NUMBER],
    #                  customer[EMAIL_ADDRESS],
    #                  customer[STATUS],
    #                  customer[CREDIT_LIMIT])
    # logger.info(DATA[0])
    # logger.info(DATA[1])
    # logger.info(DATA[2])

    # search for customers
    search_customer('C000097')
    #
    # delete customer
    delete_customer('C000099')
    #
    # update credit limit
    update_customer('C000097', '678')
    #
    # number of active customers
    list_active_customers()

    database.close()
