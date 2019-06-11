"""
inventory.py
lesson08 hw
"""
import csv
from functools import partial
import faker


def add_furniture(customer_name, item_code, item_description,
                  item_monthly_price, invoice_file="invoice.csv"):
    """This function will create an invoice_file if it doesn’t
       exist or append a new line to it if it does.

    :params invoice_file str: Filename of invoice, defaults to 'invoice.csv'
    :params customer_name str: Name of Customer
    :params item_code str: Item Code
    :params item_description str: Description of Item
    :params item_monthly_price: Monthly price of Item
    """
    row = [customer_name, item_code, item_description, item_monthly_price]
    with open(invoice_file, "a+") as invoice:
        writer = csv.writer(invoice)
        writer.writerow(row)


def single_customer(customer_name, invoice_file):
    """

    :params customer_name str: Name of Customer
    :params invoice_file str: Filename of invoice.

    :return Returns a function that takes one parameter, rental_items.
    :rtype function
    """
    part = partial(add_furniture, customer_name=customer_name,
                   invoice_file=invoice_file)
    def items(rental_items):
        with open(rental_items, "r") as test_items:
            rented_items = csv.reader(test_items)
            for item in rented_items:
                part(item_code=item[0],
                     item_description=item[1],
                     item_monthly_price=item[2])
    return items


if __name__ == "__main__":
    add_furniture(faker.Faker().name(), "JM34", "Office Chair", "34.00")
    create_invoice = single_customer(faker.Faker().name(), "invoice.csv")
    create_invoice("test_items.csv")
