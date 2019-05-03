# -------------------------------------------------#
# # Title: Lesson 03 basic_operations
# # Dev:   Justin Jameson
# # Date:  4/20/2019
# # ChangeLog: (Who, when, What)
# -------------------------------------------------#
""" This file will perform interactions with the database and gather user input.
Defining the database information and applying logging messages"""

import sys
import logging
import peewee
from customer_class import CustomerInformationClass
from customer_info_model import *
from playhouse.shortcuts import model_to_dict

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main_menu(user_prompt=None):
    """
    This method creates the menu for the program.
    The intent is to offer (3) choices:
    1: add a new customer, 2: modify the database, and 3: exit the program.
    """
    valid_prompts = {"1": create_new_customer,
                     "2": search_customer,
                     "3": delete_customer,
                     "4": update_customer_credit,
                     "5": list_active_customers,
                     "q": exit_program}
    options = list(valid_prompts.keys())

    while user_prompt not in valid_prompts:
        options_str = ("{}" + ", {}" * (len(options)-1)).format(*options)
        # look at the format string with the use of f and options at the end.
        print(f"Please choose from the following options ({options_str}):")
        print("1. Add a new Customer to the DataBase")
        print("2. Search the DataBase for a Customer")
        print("3. Delete a Customer from the DataBase")
        print("4. Update the Customer's credit line")
        print("5. List all active Customers")
        print("q. Quit")
        user_prompt = input(">")
    return valid_prompts.get(user_prompt)


def create_new_customer():
    new_customer = CustomerInformationClass(
        customer_id=input("Enter Customer ID: "),
        first_name=input("Enter Customers first name: "),
        last_name=input("Enter Customers last name: "),
        home_address=input("Enter the Customers Home Address: "),
        phone_number=input("Enter the Customers Phone Number: "),
        email_address=input("Enter the Customers Email: "),
        customer_status=input("Enter the Customers Status (Active/Inactive):"),
        credit_limit=input("Enter the Customers Credit Limit: "))
    logger.info('create_new _customer parameters entered.')
    customer_info = new_customer.return_as_dictionary()
    add_customer(customer_info)


def add_customer(customer_dict):  # customer_id, name, lastname, home_address, phone_number, email_address, status, credit_limit):
    """This function will add a new customer to the sqlite3 database."""
    try:
        new_customer = Customer.create(
            customer_id=customer_dict['customer_id'],
            first_name=customer_dict['first_name'],
            last_name=customer_dict['last_name'],
            home_address=customer_dict['home_address'],
            phone_number=customer_dict['phone_number'],
            email_address=customer_dict['email_address'],
            customer_status=customer_dict['customer_status'],
            credit_limit=customer_dict['credit_limit'])  # Record created
        new_customer.save()  # Record saved
        logger.info('Database add successful')
        logger.info(customer_dict)

    except Exception as e:
        logger.info(f'Error creating = {customer_dict}')
        logger.info(e)
        logger.info('See how the database protects our data')

    main_menu()()


def search_customer(customer_id=None):
    """This function will return a dictionary object with name, lastname,
    email address and phone number of a customer or an empty dictionary object
    if no customer was found."""
    if customer_id is None:
        customer_id = input("Enter Customer ID: ")
    else:
        customer_id = customer_id
    query_dict = {}
    try:
        query = (
            Customer
            .select()
            .where(Customer.customer_id == customer_id).get())
        query_dict = model_to_dict(query)
    except peewee.DoesNotExist:
        logger.info("Can't find customer with id: %s.", customer_id)
        logger.info("Returning empty dict.")
    print(query_dict)
    return query_dict


def delete_customer(customer_id=None):
    """This function will delete a customer from the sqlite3 database."""
    dbase = Customer
    if customer_id is None:
        customer_id = input("Enter Customer ID: ")
    else:
        customer_id = customer_id
    try:
        remove_customer = dbase.get(dbase.customer_id == customer_id)
        remove_customer.delete_instance()
        logger.info('Database delete successful')

    except Exception as e:
        logger.info(f'Error finding = {customer_id}')
        logger.info(e)


def update_customer_credit(customer_id=None, new_credit=None):
    """This function will search an existing customer by customer_id
    and update their credit limit or raise a ValueError exception
    if the customer does not exist."""
    if customer_id is None and new_credit is None:
        customer_id = input("Enter Customer ID: ")
        new_credit = input("Enter new credit limit: ")
    else:
        customer_id = customer_id
        new_credit = new_credit

    with database.transaction():
        update = (
            Customer
            .update(credit_limit=new_credit)
            .where(Customer.customer_id == customer_id)
            .execute()
        )
    if update == 0:
        logger.info("No customer was found for id %s", customer_id)
        raise ValueError("NoCustomer")
    return update


def list_active_customers():
    """This function will return an integer with the number of customers
    whose status is currently active."""
    try:
        active_customers = (
            Customer
            .select()
            .where(Customer.customer_status == "A").count())
    except peewee.DoesNotExist:
        logger.info("No active customers found in DB")
    print(active_customers)

def exit_program():
    """This method exits the program"""
    logger.info('called exit_program')
    sys.exit()


if __name__ == '__main__':
    while True:
        main_menu()()
        input("Press Enter to continue...........")
