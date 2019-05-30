#!/usr/bin/env python3
''' Create and read inventory csv files.  Lesson08 homework. '''

import os
from functools import partial

def add_furniture(invoice_file, customer_name, item_code,
                  item_description, item_monthly_price):
    ''' The function which actually adds data to a file '''
    write_header = not os.path.isfile(invoice_file)
    fil = open(invoice_file, 'a+')
    if write_header:
        fil.write("customer_name,item_code,item_description,item_monthly_price\n")
    fil.write("%s,%s,%s,%s\n" % (customer_name, item_code, item_description, item_monthly_price))
    fil.close()

def single_customer(customer_name, invoice_file):
    ''' Generator returns a function that adds a list of items '''
    customer_add_furniture = partial(add_furniture, invoice_file=invoice_file,
                                     customer_name=customer_name)
    def add_items_for_customer(rental_items):
        for item in rental_items:
            customer_add_furniture(**item)
    return add_items_for_customer

# simple test mode if run from the cli
if __name__ == "__main__":
    print("Adding furniture.")
    ADDER = single_customer("Bob Barker", "inventory.csv")
    ITEMS = [
        {'item_code': 'DSK01', 'item_description': 'Office Desk', 'item_monthly_price': 10.01},
        {'item_code': 'LMP52', 'item_description': 'Desk Lamp', 'item_monthly_price': 1.61},
        {'item_code': 'CHR19', 'item_description': 'Office Chair', 'item_monthly_price': 5.22}
    ]
    ADDER(ITEMS)
