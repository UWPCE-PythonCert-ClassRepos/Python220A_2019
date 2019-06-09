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

    logging.debug(f'Appending data to file {type(csv_data)}: {csv_data}')

    with open(invoice_file, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(csv_data)


def single_customer(customer_name, invoice_file):
    """Iterate through rental_items and add each item to invoice_file."""

    # Create a function called single_customer:
    # Input parameters: customer_name, invoice_file.
    # Output: Returns a function that takes one parameter, rental_items.
    # single_customer needs to use functools.partial and closures, in order to
    # return a function that will iterate through rental_items and add each
    # item to invoice_file.

    a = partial(add_furniture, customer_name=customer_name,
                invoice_file=invoice_file)

    def create_invoice(rental_items):
        with open(rental_items, 'r') as csv_file:
            reader = csv.reader(csv_file)

            for row in reader:
                a(item_code=row[0],
                  item_description=row[1],
                  item_monthly_price=row[2]
                  )
        return a
    return create_invoice


def add_initial_data(file):
    # Add initial data using faker
    # my_word_list = [
    #     'Sofa', 'TV', 'Refrigerator',
    #     'Love Seat', 'Table', 'Desk',
    #     'Dinning Table', 'Oven', 'Stove',
    #     'Dishwasher', 'TV Stand', 'Bookcase', 'Radio']
    #
    # invoice_file = '../data/invoice_file.csv'
    #
    # for i in range(10):
    #     customer_name = fake.name()
    #     item_code = fake.password(length=4, special_chars=False, digits=True,
    #                               upper_case=True, lower_case=False)
    #     item_description = fake.safe_color_name().title() + ' ' + \
    #         fake.word(ext_word_list=my_word_list)
    #     item_monthly_price = random.randint(5, 201)
    #
    #     add_furniture(invoice_file, customer_name, item_code,
    #                   item_description, item_monthly_price)

    # Add initial data from hardcoded list

    # invoice_data = [
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
    # ]
    #
    logging.debug('Initializing invoice file...')
    logging.debug('Generating fake data...')
    initial_invoice_data = generate_fake_data()
    print(initial_invoice_data)
    # logging.debug('{}fake records generated.'.format(
    #     type(initial_invoice_data), initial_invoice_data.count()))

    # with open(file, 'w', newline='') as csv_file:

        # for invoice in initial_invoice_data:
            # logging.debug(invoice)
            # add_furniture(invoice_file, invoice[0], invoice[1],
            #               invoice[2], invoice[3])
            # add_furniture(invoice_file, *invoice_data)


def generate_fake_data():
    # Using Faker
    # Add initial data using faker
    # my_word_list = [
    #     'Sofa', 'TV', 'Refrigerator',
    #     'Love Seat', 'Table', 'Desk',
    #     'Dinning Table', 'Oven', 'Stove',
    #     'Dishwasher', 'TV Stand', 'Bookcase', 'Radio']
    #
    # invoice_file = '../data/invoice_file.csv'
    # fake_data = []
    # for i in range(10):
    #     customer_name = fake.name()
    #     item_code = fake.password(length=4, special_chars=False, digits=True,
    #                               upper_case=True, lower_case=False)
    #     item_description = fake.safe_color_name().title() + ' ' + \
    #         fake.word(ext_word_list=my_word_list)
    #     item_monthly_price = random.randint(5, 201)
    # FIXME
        # add_furniture(invoice_file, customer_name, item_code,
        #               item_description, item_monthly_price)
    #      fake_data.append(customer_name, item_code,
    #                   item_description, item_monthly_price)

    fake_data = [
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
        ]
    logging.debug(type(fake_data))
    return fake_data


def main():
    pass


if __name__ == '__main__':
    invoice_file = '../data/invoice_file.csv'
    add_initial_data(invoice_file)

    # initialize_file = 'Y'
    # initialize_file = input('Start Fresh? ')
    # if initialize_file.upper() == 'Y':
    #     add_initial_data(invoice_file, initial_invoice_data)
    #
    # main(invoice_file, invoice_data)
