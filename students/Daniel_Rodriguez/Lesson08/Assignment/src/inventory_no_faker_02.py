# --------------------------------------------------------------------------- #
# Course: PYTHON 220: Advanced Programming in Python
# Script Title: Lesson 8 Assignment
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-05-27, Initial release
# --------------------------------------------------------------------------- #

import logging
from functools import partial
import csv
from pprint import pprint as print
# import random
# from faker import Faker
# fake = Faker()


logging.basicConfig(level=logging.DEBUG)


def add_furniture(invoice_file, customer_name, item_code, item_description,
                  item_monthly_price):
    """This function will create invoice_file"""

    csv_data = [customer_name, item_code, item_description,
                item_monthly_price]

    # logging.debug(f'Appending data to file {type(csv_data)}: {csv_data}')
    logging.debug(f'Opening Invoice Items file for appending: {invoice_file}')
    with open(invoice_file, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        logging.debug(f'Writing Invoice Items file for appending: {invoice_file}')
        writer.writerow(csv_data)


def single_customer(customer_name, invoice_file):
    """Iterate through rental_items and add each item to invoice_file."""

    # Create a function called single_customer:
    # Input parameters: customer_name, invoice_file.
    # Output: Returns a function that takes one parameter, rental_items.
    # single_customer needs to use functools.partial and closures, in order to
    # return a function that will iterate through rental_items and add each
    # item to invoice_file.

    logging.debug('Inside single_customer function...')
    rental_items = '../data/rental_items.csv'
    logging.debug(f'Processing rental items for {customer_name} from file {rental_items}')

    a = partial(add_furniture, customer_name=customer_name,
                invoice_file=invoice_file)

    def create_invoice(rental_items):
        logging.debug(f'opening Rental Items file for reading: {rental_items}')
        with open(rental_items, 'r') as csv_file:
            reader = csv.reader(csv_file)
            logging.debug('Reading Rental Items file...')
            for row in reader:
                logging.debug(f'Adding Rental Item {row}')
                a(item_code=row[0],
                  item_description=row[1],
                  item_monthly_price=row[2]
                  )
        return a
    return create_invoice


def add_initial_data(invoice_file):
    logging.debug(f'Creating new Invoice file in "{invoice_file}"')
    invoice_data = (
        ['Elisa Miles', 'LR04', 'Lime Bookcase', 25],
        ['Laura Peterson', '7AJI', 'Maroon Stove', 104],
        ['Brent Wallace', 'FF5K', 'Blue Stove', 59],
        ['Laura Carter', '21RH', 'Lime Bookcase', 54],
        ['Timothy Church PhD', 'EA4W', 'Navy Table', 60],
        ['Emily Bauer', '0YUX', 'Gray Desk', 165],
        ['Lori Montgomery', '5IK3', 'Gray TV Stand', 47],
        ['Julie Ford', '2QA5', 'Silver TV', 49],
        ['Diane Lopez', '7E4E', 'Blue Refrigerator', 18],
        ['William Martinez', '6E5F', 'Lime Table', 18]
        )

    with open(invoice_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        for data in invoice_data:
            logging.debug(f'Adding Data to Invoice File: {data}')
            writer.writerow(data)


def main():
    invoice_file = '../data/invoice_file.csv'

    initialize_file = 'N'
    # initialize_file = input('Start Fresh? ')
    if initialize_file.upper() == 'Y':
        logging.debug('Starting with an empty file')
        add_initial_data(invoice_file)
    else:
        logging.debug(f'Adding records to existing Invoice file: {invoice_file}')

    # rental_items = '../data/rental_items.csv'

    customer_name = 'Elisa Miles'
    logging.debug(f'Adding rental items for {customer_name}')
    single_customer(customer_name, invoice_file)


if __name__ == '__main__':
    main()
