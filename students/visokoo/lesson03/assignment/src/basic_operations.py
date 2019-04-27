"""
    A compilation of methods for interacting with an ORM DATABASE
"""

import logging
from playhouse.shortcuts import model_to_dict
from src.models import DATABASE, Customer, peewee

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)


def add_customer(customer_id,
                 name,
                 last_name,
                 home_address,
                 phone_number,
                 email_address,
                 status,
                 credit_limit):
    """add_customer(customer_id, name, last_name, home_address, phone_number,
                    email_address, status, credit_limit)

    Add customer info into DB based on provided params.

    :param customer_id str: Unique customer ID
    :param name str: First name of customer
    :param last_name str: Last name of customer
    :param str: Phone number of customer
    :param email_address str: Email address of customer
    :param status str: Active or Inactive customer
    :param credit_limit int: Credit limit for customer

    :return None
    :rtype None
    """
    try:
        with DATABASE.transaction():
            new_customer = Customer.create(
                customer_id=customer_id,
                name=name,
                last_name=last_name,
                home_address=home_address,
                phone_number=phone_number,
                email_address=email_address,
                status=status,
                credit_limit=credit_limit)
            LOGGER.info("DATABASE add successful")
    except peewee.IntegrityError:
        LOGGER.info("Unique constraint failed on %s", customer_id)


def search_customer(customer_id):
    """search_customer(customer_id)

    Search for a customer via provided customer_id in DB.
    Returns the object in dict format.

    :param customer_id str: Unique customer ID

    :return dict representation of existing customer, empty dict
    if not found.
    :rtype dict
    """
    query_dict = {}
    try:
        query = (
            Customer
            .select()
            .where(Customer.customer_id == customer_id).get())
        query_dict = model_to_dict(query)
    except peewee.DoesNotExist:
        LOGGER.info("Can't find customer with id: %s.", customer_id)
        LOGGER.info("Returning empty dict.")
    return query_dict


def delete_customer(customer_id):
    """delete_customer(customer_id)

    Search for a customer via provided customer_id in DB.
    Run delete_instance() on the selected item so we can cascade delete
    if there are dependents. Will throw an error message if the customer
    cannot be found.

    Returns True if the deletion was successful.

    :param customer_id str: Unique customer ID

    :return Return true if the customer was deleted.
    :rtype boolean
    """
    try:
        with DATABASE.transaction():
            query = (
                Customer
                .select()
                .where(Customer.customer_id == customer_id).get())
            query.delete_instance(recursive=True)
            LOGGER.info(
                "Deleted customer: %s.", customer_id)
            return True
    except peewee.DoesNotExist:
        LOGGER.info(
            "Can't find customer with id to delete: %s.", customer_id)


def list_active_customers():
    """list_active_customers()

    Queries the DB and returns an integer with the number of customers
    whose status is currently active.

    :return total count of active customers
    :rtype int
    """
    try:
        active_customers = (
            Customer
            .select()
            .where(Customer.status == "active").count())
    except peewee.DoesNotExist:
        LOGGER.info("No active customers found in DB")
    return active_customers


def update_customer_credit(customer_id, new_credit):
    """update_customer_credit(customer_id, new_credit)

    Queries the DB for a matching customer_id and updates their
    credit limit with the new_credit param.

    :param customer_id str: Unique customer ID
    :param new_credit int: Credit limit of customer as int

    :return total rows updated unless rows updated < 1
    :rtype int
    """
    with DATABASE.transaction():
        update = (
            Customer
            .update(credit_limit=new_credit)
            .where(Customer.customer_id == customer_id)
            .execute()
        )
    if update == 0:
        LOGGER.info("No customer was found for id %s", customer_id)
        raise ValueError("NoCustomer")
    return update


def delete_all_rows():
    """delete_all_rows()

    Deletes all data from the Customer table so we can
    have fresh tests.

    """
    with DATABASE.transaction():
        Customer.delete().execute()
        LOGGER.info("Clear all data in Customer table.")
