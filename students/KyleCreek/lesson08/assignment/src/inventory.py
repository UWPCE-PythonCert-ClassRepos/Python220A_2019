import csv
from functools import partial
import os


def add_furniture(invoice_file, customer_name, item_code, item_description, item_monthly_price):
    """
    Creates or appends an invoice file
    :param invoice_file: Name of invoice file
    :param customer_name: Customer's Name
    :param item_code: Item Code
    :param item_description: Description of Item
    :param item_monthly_price: Cost of Item per month
    :return: Stores an invoice file to hard Drive
    """

    # Establish file directory for .csv file
    base_path = "C:\\Python220A_2019\\students\\KyleCreek\\lesson08\\assignment\\data\\"
    file_path = base_path + invoice_file
    item_monthly_price = float(item_monthly_price)
    # Store data in a list to place into .csv file
    data = [customer_name,
            item_code,
            item_description,
            '{:.2f}'.format(item_monthly_price)]

    # Case statements to handle whether invoice file currently exists.
    if os.path.exists(file_path):
        csv_mode = 'a'
    else:
        csv_mode = 'w'

    # Write/Append to Invoice File
    with open(file_path, csv_mode, newline='') as csv_file_out:
        csv_writer = csv.writer(csv_file_out)
        csv_writer.writerow(data)


def single_customer(customer_name, invoice_file):
    """
    Returns a function that will add to invoice file
    :param customer_name: Name of the Customer
    :param invoice_file: Name of the invoice_file
    :return: Function that will add to a file
    """
    def add_invoice(rental_items):
        """
        Reads the list of items and adds to an invoice
        :param .csv file containing rental items
        :return: Writes to invoice .csv file
        """
        # Create partial function for inner function
        partial_add = partial(add_furniture, invoice_file=invoice_file, customer_name=customer_name)

        # Create .csv File handler
        with open(rental_items, 'r') as csv_file_in:
            # Read Each Row in the .csv file
            for row in csv.reader(csv_file_in):
                # Associate data with keyword arguments
                partial_add(item_code=row[0],
                            item_description=row[1],
                            item_monthly_price=row[2])
    return add_invoice

new_fun = single_customer("Kyle", 'test')
csv_file = "C:\\Python220A_2019\\students\\KyleCreek\\lesson08\\assignment\\data\\test_items.csv"
new_fun(csv_file)
