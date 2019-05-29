# **************************
# Title: inventory.py
# Desc:
# 1. Create a python module called inventory.py, to replace the existing spreadsheet.
# 2. Create a function called add_furniture that takes the following input parameters:
#         invoice_file
#         customer_name
#         item_code
#         item_description
#         item_monthly_price
# This function will create invoice_file (to replace the spreadsheet’s data)
# if it doesnt exist, or append a new line to it if it does exist.
#
# 3. Create a function called single_customer:
#        Input parameters: customer_name, invoice_file.
#        Output: Returns a function that takes one parameter, rental_items.
# single_customer needs to use functools.partial and closures, in order to return a function
# that will iterate through rental_items and add each item to invoice_file.
#
# should write a try catch block to identify if items are not included such as if item no has more than len(4) error.
#
# Change Log: (Who, When, What)
# Justin Jameson, 20190525, created file
#
# **************************
import sys
import datetime
import csv
import logging

existing_invoice_file = '../data/rented_items.csv'


def add_furniture(invoice_file=existing_invoice_file, customer_name='Name',
                  item_code='Item', item_description='Description', item_monthly_price='Price'):
    """
    This function creates invoice_file if it does not exist, or appends a new line to it if it does exist.
    :param invoice_file: The name of the csv file(s) that will be added to the master (single_customer) invoice.
    :param customer_name: The name of the Customer who rented the furniture.
    :param item_code: The coding identifier for the rented furniture.
    :param item_description: A short description of the furniture.
    :param item_monthly_price: The amount rental amount for the furniture.
    :return:
    """
    with open(invoice_file, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"')
        new_row = [customer_name, item_code, item_description, item_monthly_price]
        writer.writerow(new_row)


def single_customer(customer_name, invoice_file):
    """
    This function imports a csv file, reads the rows, then writes the row to the invoice csv file.
    :param customer_name: A single customer with multiple rentals.
    :param invoice_file: File that the invoice will write to (database).
    :return:
    """

    # open csv file and read lines.
    with open(invoice_file, 'r', newline='') as rcsvfile:
        reader = csv.reader(rcsvfile, delimiter=',', quotechar='"')
        for row in reader:
            # write to the invoice to file.
            def invoice_file(item_code, item_description, item_monthly_price):
                with open(existing_invoice_file, 'a', newline='') as wcsvfile:
                    writer = csv.writer(wcsvfile, delimiter=',', quotechar='"')
                    new_row = [customer_name, item_code, item_description, item_monthly_price]
                    writer.writerow(new_row)
                return print(new_row)
            invoice_file(row[0], row[1], row[2])


if __name__ == "__main__":
    add_furniture("../data/rented_items.csv", "Elisa Miles", "LR04", "Leather Sofa", 25)
    add_furniture("../data/rented_items.csv", "Edward Data", "KT78", "Kitchen Table", 10)
    add_furniture("../data/rented_items.csv", "Alex Gonzales", "QM83", "Queen Mattress", 17)
    create_invoice = single_customer("Susan Wong", "../data/test_items.csv")
