"""
Operations class to create, remove, update, and delete customer data
"""

from customer_model import *
import logging
import csv

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
    :return: Customer table
    """
    try:

        logger.info("Create Customer record")

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
            logger.info(f'Successfully added new customer: {new_customer}')
            logger.info(f'id: {new_customer.customer_id}')
            logger.info(f'first: {new_customer.first_name}')
            logger.info(f'last: {new_customer.first_name}')
            logger.info(f'address: {new_customer.home_address}')
            logger.info(f'phone: {new_customer.phone_number}')
            logger.info(f'email: {new_customer.email_address}')
            logger.info(f'status: {new_customer.status}')
            logger.info(f'limit: {new_customer.credit_limit}')

    except Exception as e:

        logger.warning(f'Error creating customer: {cust_id}')
        logger.warning(e)

    return Customer


def search_customer(customer_id):
    """
    search & return customer based on id
    :return: (dict) Customer
    """

    with database.transaction():
        query = (Customer.select(Customer)
                 .where(Customer.customer_id == customer_id))

    logger.info('create dictionary of query results by iterating through query')
    results = {}
    for result in query:
        results['first_name'] = result.first_name
        results['last_name'] = result.last_name
        results['email_address'] = result.email_address
        results['phone_number'] = result.phone_number
    logger.info(results)

    if not bool(results):
        logger.warning('No such customer exits')

    return results


def delete_customer(customer_id):
    try:
        with database.transaction():
            customer = Customer.get(Customer.customer_id == customer_id)
            logger.info(f'User wishes to delete: {customer}')
            customer.delete_instance()
            logger.info(f'Successfully deleting: {customer}')

        return True

    except Exception as e:

        logger.warning(f'Error deleting customer: {customer_id}')
        logger.warning(e)

    return False


def update_customer(customer_id, credit_limit):
    try:
        with database.transaction():
            customer_update = Customer.get(Customer.customer_id == customer_id)
            logger.info(f'limit before update: {customer_update.credit_limit}')
            customer_update.credit_limit = credit_limit
            logger.info(f'limit post update: {customer_update.credit_limit}')

        return True

    except Exception as e:

        logger.warning(f'Error updating customer: {customer_id}')
        logger.warning(e)

    return False


def list_active_customers():
    """

    :return:
    """
    with database.transaction():
        query = (Customer.select(fn.COUNT(Customer.status)
                                 .alias('count')).where(Customer.status))
        logger.info(query)

    customer_count = []
    for item in query:
        logger.info(f'Number of active customers {item.count}')
        customer_count.append(item.count)
    return customer_count[0]


if __name__ == '__main__':
    customers = [
        [1, 'Harry', 'Potter', '234 Wizard Wd',
         5554328765, 'hpotter@hogarts.com', True, 150000],
        [2, 'Mario', 'Kart', '567 Racekart Wy',
         5556789012, 'mrmario@magic.com', False, 25000],
        [3, 'Spongebob', 'Squarepants', '890 Pineapplehouse Ct',
         5556543210, 'bob@gmail.com', True, 10000],
    ]

    #  attempt to import customer csv, kept getting datatype mismatch #
    #  error even when changing the customer_model                    #

    # customers = []
    # with open(r'C:\Python220\Python220A_2019\students\kevin_cavanaugh'
    #           r'\Lesson03\assignment\data\customer.csv',
    #           encoding='utf-8', errors='ignore') as people:
    #     customer_reader = csv.reader(people)
    #     for row in customer_reader:
    #         customers.append(row)

    database.create_tables([Customer])
    logging.info(f'Created table: {Customer.__name__}')

    #  add customers
    for customer in customers:
        add_customer(customer[CUSTOMER_ID],
                     customer[FIRST_NAME],
                     customer[LAST_NAME],
                     customer[HOME_ADDRESS],
                     customer[PHONE_NUMBER],
                     customer[EMAIL_ADDRESS],
                     customer[STATUS],
                     customer[CREDIT_LIMIT])
    logger.info(customers[0])
    logger.info(customers[1])
    logger.info(customers[2])

    # search for customers
    search_customer(45)

    # delete customer
    delete_customer(1)

    # update credit limit
    update_customer(2, 450000)

    # number of active customers
    list_active_customers()

    database.close()
