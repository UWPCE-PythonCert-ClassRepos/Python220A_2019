from functools import partial
import csv

existing_invoice_file = '../data/rented_items.csv'

def add_furniture(invoice_file='existing_invoice_file', customer_name='Name',
                  item_code='Item', item_description='Description', item_monthly_price='Price'):
    print(invoice_file, customer_name, item_code,item_description, item_monthly_price)


def single_customer(customer_name, invoice_file):
    with open(invoice_file, 'r', newline='') as rcsvfile:
        reader = csv.reader(rcsvfile, delimiter=',', quotechar='"')
        for row in reader:
            mult_entry_single_customer = partial(add_furniture, existing_invoice_file, customer_name)
            # mult_entry_single_customer('lro4', 'leather sofa', 25)
            mult_entry_single_customer(row[0], row[1], row[2])


add_furniture("../data/rented_items.csv", "Elisa Miles", "LR04", "Leather Sofa", 25)
add_furniture("../data/rented_items.csv", "Edward Data", "KT78", "Kitchen Table", 10)
add_furniture("../data/rented_items.csv", "Alex Gonzales", "QM83", "Queen Mattress", 17)
single_customer("Susan Wong", "../data/test_items.csv")

# mult_entry_single_customer = single_customer("Susan Wong", "../data/test_items.csv")
# mult_entry_single_customer('lro4', 'leather sofa', 25)


# ***************************************************************
#  # mult_entry_single_customer = partial(add_furniture, customer_name, invoice_file)
#     # open csv file and read lines.
#     with open(invoice_file, 'r', newline='') as rcsvfile:
#         reader = csv.reader(rcsvfile, delimiter=',', quotechar='"')
#         for row in reader:
#             mult_entry_single_customer = partial(add_furniture, customer_name, existing_invoice_file)
#             mult_entry_single_customer(row[0], row[1], row[2])
#             print(row)
#             print(mult_entry_single_customer(row[0], row[1], row[2]))
#             # write to the invoice to file.
#             # def invoice_file(item_code, item_description, item_monthly_price):
#             #     with open(existing_invoice_file, 'a', newline='') as wcsvfile:
#             #         writer = csv.writer(wcsvfile, delimiter=',', quotechar='"')
#             #         new_row = [customer_name, item_code, item_description, item_monthly_price]
#             #         writer.writerow(new_row)
#             #     return print(new_row)
#             # invoice_file(row[0], row[1], row[2])