# ---------------------------------------------------------------------------- #
# Course: PYTHON 220: Advanced Programming in Python
# Script Title: Lesson 8 Assignment
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-05-27, Initial release
# ---------------------------------------------------------------------------- #

import logging
import random
import csv
from faker import Faker
fake = Faker()


logging.basicConfig(level=logging.DEBUG)


def add_furniture(invoice_file, customer_name, item_code, item_description,
                  item_monthly_price):
    """This function will create invoice_file"""

    csv_data = [customer_name, item_code, item_description,
                item_monthly_price]

    logging.debug(f'Adding to file {type(csv_data)}: {csv_data}')

    with open(invoice_file, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(csv_data)


def single_customer(customer_name, invoice_file):
    """Iterate through rental_items and add each item to invoice_file."""

    # Create a function called single_customer:
    # Input parameters: customer_name, invoice_file.
    # Output: Returns a function that takes one parameter, rental_items.
    # single_customer needs to use functools.partial and closures, in order to
    # return a function that will iterate through rental_items and add each item
    # to invoice_file.

    pass


def main():
    my_word_list = [
        'Sofa', 'TV', 'Refrigerator',
        'Love Seat', 'Table', 'Desk',
        'Dinning Table', 'Oven', 'Stove',
        'Dishwasher', 'TV Stand', 'Bookcase', 'Radio']

    invoice_file = '../data/invoice_file.csv'

    for i in range(10):
        customer_name = fake.name()
        item_code = fake.password(length=4, special_chars=False, digits=True,
                                  upper_case=True, lower_case=False)
        item_description = fake.safe_color_name().title() + ' ' + \
            fake.word(ext_word_list=my_word_list)
        item_monthly_price = random.randint(5, 201)

        add_furniture(invoice_file, customer_name, item_code,
                      item_description, item_monthly_price)


if __name__ == '__main__':
    main()
