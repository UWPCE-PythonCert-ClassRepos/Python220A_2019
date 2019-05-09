
import logging
import csv
from customers_db_schema import *


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def add_customer(customer_id, name, last_name, home_address,
                 phone_number, email_address, status, credit_limit):
    '''
    This function takes inputs of customer data and adds the data to the database.
    :param customer_id:
    :param name:
    :param last_name:
    :param home_address:
    :param phone_number:
    :param email_address:
    :param status:
    :param credit_limit:
    :return:
    '''

    try:
        with database.transaction():
            new_customer = Customer.create(
                cust_id = customer_id,
                cust_name = name,
                cust_last_name = last_name,
                cust_home_address = home_address,
                cust_phone = phone_number,
                cust_email = email_address,
                cust_status = status,
                cust_credit_limit = credit_limit
            )
            new_customer.save()
            logger.info('Add Customer successful')
    except Exception as e:
        logger.info(f'Error creating = {[customer_id]}')
        logger.info(e)

def search_customer(cust_id):
    '''
    Search customer function works by selecting the customer data that matches
    the customer id parameter.
    :param customer_id:
    :return: query_dict
    '''
    try:
        ###removed transaction method###
        ###and replaced 'select' with 'get' method.###
        # with database.transaction():
        # query = (Customer.select().where(
        # Customer.cust_id == customer_id).get())

        query = (Customer.get(Customer.cust_id == cust_id))

        query_dict = {'cust_id': query.cust_id,
                      'cust_name': query.cust_name,
                      'cust_last_name': query.cust_last_name,
                      'cust_email': query.cust_email,
                      'cust_phone': query.cust_phone
                      }

        logger.info(f'The following cutomer information has been selected:'
                    f'{query_dict}')

        return query_dict

    except Exception as e:
        logger.info('search customer unsuccessful.')
        logger.info(e)

def delete_customer(customer_id):
    '''
    Delete customer function will delete a row of data that equals
    the customer id parameter.
    :param customer_id:
    :return:
    '''
    try:
        with database.transaction():
            # changed method from 'select' to get
            # query = (Customer.select().where(Customer.cust_id == customer_id).get())
            query = (Customer.get(Customer.cust_id == customer_id))
            query.delete_instance()
            logger.info(f'Deleting {Customer.cust_id}')
            return True

    except Exception as e:
        logger.info(f'Delete failed: {Customer.cust_id}')
        logger.info(e)

def update_customer_credit(customer_id, credit_limit):
    '''
    This function will search an existing customer by customer id
    and update their credit limit or raise a ValueError
    exception if the customer does not exist
    :param customer_id:
    :param credit_limit:
    :return:
    '''

    try:
        with database.transaction():
            q = (Customer
                 .update(cust_credit_limit = credit_limit)
                 .where(Customer.cust_id == customer_id)
                 .execute())
            logger.info(f'Customer, {customer_id} credit limit updated to '
                        f'${credit_limit}')

        if q == 0:
            logger.info(f'Customer, {customer_id} '
                        f'could not update ${credit_limit}')

        else:
            raise ValueError("NoCustomer")

    except Exception as v:
        logger.info(v)
        logger.info(f'transaction failed for {customer_id}')

    return q

def list_active_customers():
    '''
    This function will return an integer with the number
    of customers whose status is currently active.
    :return:
    '''

    ##Update##
    # changed query to search for 'Active', not 'active'
    # csv has actives as 'Active'
    
    try:
        with database.transaction():
            query = (Customer.select()
                     .where(Customer.cust_status == 'Active'))\
                     .count()
            logger.info(f'the number of active customers is {query}')

    except Exception as a:
        logger.info(f'failed query active customers')
        logger.info(a)

    return query

def load_customer_data(data_source):
    '''
    Iterates through input csv file for adding data to the
    database.
    :param data_source:
    :return:
    '''

    with open(data_source) as f:
        while True:
            try:
                value = next(csv.reader(f))
                yield tuple(value)

            except StopIteration as s:
                logger.info(s)
                logger.info(f"All data in {data_source} added.")
                break


