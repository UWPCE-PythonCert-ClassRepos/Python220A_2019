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
import random
from faker import Faker

fake = Faker()


logging.basicConfig(level=logging.DEBUG)


def add_furniture(invoice_file, customer_name, item_code, item_description,
                  item_monthly_price):
    """This function will create invoice_file"""

    csv_data = [customer_name, item_code, item_description,
                item_monthly_price]

    # logging.debug(f'Appending data to file {type(csv_data)}: {csv_data}')
    logging.debug(f'Opening Invoice Items file for appending: '
                  f'"{invoice_file}"')
    with open(invoice_file, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        logging.debug(f'Writing {csv_data} to Invoice Items file: '
                      f'"{invoice_file}"')
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
    # rental_items = '../data/rental_items.csv'
    # logging.debug(f'Processing rental items for {customer_name} '
    #               f'from file "{rental_items}"')

    partial_add_furniture = partial(add_furniture,
                                    invoice_file=invoice_file,
                                    customer_name=customer_name)

    def create_invoice(rental_items):
        logging.debug(f'Opening Rental Items file for reading: '
                      f'"{rental_items}"')

        with open(rental_items, 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            logging.debug(f'Reading Rental Items file...')
            for row in reader:
                logging.debug(f'Reading data {row} from Rental Items file '
                              f'"{rental_items}"')

                partial_add_furniture(item_code=row[0],
                                      item_description=row[1],
                                      item_monthly_price=row[2]
                                      )
        return partial_add_furniture
    return create_invoice


def add_initial_data(invoice_file):
    logging.debug(f'Creating new Invoice file in "{invoice_file}"')

    # Hardcoded initial data set
    # invoice_data = (
    #     ['Elisa Miles', 'LR04', 'Lime Bookcase', 25],
    #     ['Laura Peterson', '7AJI', 'Maroon Stove', 104],
    #     ['Brent Wallace', 'FF5K', 'Blue Stove', 59],
    #     ['Laura Carter', '21RH', 'Lime Bookcase', 54],
    #     ['Timothy Church PhD', 'EA4W', 'Navy Table', 60],
    #     ['Emily Bauer', '0YUX', 'Gray Desk', 165],
    #     ['Lori Montgomery', '5IK3', 'Gray TV Stand', 47],
    #     ['Julie Ford', '2QA5', 'Silver TV', 49],
    #     ['Diane Lopez', '7E4E', 'Blue Refrigerator', 18],
    #     ['William Martinez', '6E5F', 'Lime Table', 18]
    #     )
    #
    # with open(invoice_file, 'w', newline='') as csv_file:
    #     writer = csv.writer(csv_file)
    #
    #     for data in invoice_data:
    #         logging.debug(f'Adding Data to Invoice File: {data}')
    #         writer.writerow(data)

    # Using Faker to gfenerate initial data set
    my_word_list = [
        'Sofa', 'TV', 'Refrigerator',
        'Love Seat', 'Table', 'Desk',
        'Dinning Table', 'Oven', 'Stove',
        'Dishwasher', 'TV Stand', 'Bookcase', 'Radio']

    with open(invoice_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        for i in range(10):
            customer_name = fake.name()
            item_code = fake.password(length=4, special_chars=False,
                                      digits=True,
                                      upper_case=True, lower_case=False)
            item_description = fake.safe_color_name().title() + ' ' + \
                               fake.word(ext_word_list=my_word_list)
            item_monthly_price = random.randint(5, 201)

            csv_data = [customer_name, item_code, item_description,
                        item_monthly_price]

            writer.writerow(csv_data)


def main():
    invoice_file = '../data/invoice_file.csv'

    initialize_file = 'Y'
    # initialize_file = input('Start Fresh? ')
    if initialize_file.upper() == 'Y':
        logging.debug('Starting with an empty file')
        add_initial_data(invoice_file)
    else:
        logging.debug(f'Adding records to existing Invoice file:'
                      f' "{invoice_file}"')

    rental_items = '../data/rental_items.csv'

    customer_name = fake.name()
    logging.debug(f'Adding rental items for {customer_name}')
    print(type(single_customer(customer_name, invoice_file)))

    new_rental = single_customer(customer_name, invoice_file)
    new_rental(rental_items)

    # Test Partial function ---------------------------------------------------
    # partial_add_furniture = partial(add_furniture,
    #                                 invoice_file=invoice_file,
    #                                 customer_name=customer_name)
    # partial_add_furniture(item_code='XXXX',
    #                       item_description='Test Item',
    #                       item_monthly_price=69)
    # -------------------------------------------------------------------------


if __name__ == '__main__':
    main()
