import csv


def single_customer(customer_name, invoice_file):
    # open csv file and read lines.
    with open(invoice_file, 'r', newline='') as rcsvfile:
        reader = csv.reader(rcsvfile, delimiter=',', quotechar='"')
        for row in reader:
            # write to the invoice to file.
            def simple_intro(item_code, item_description, item_monthly_price):
                with open('../data/test_invoice_file.csv', 'a', newline='') as wcsvfile:
                    writer = csv.writer(wcsvfile, delimiter=',', quotechar='"')
                    new_row = [customer_name, item_code, item_description, item_monthly_price]
                    writer.writerow(new_row)
                return print(new_row)
            simple_intro(row[0], row[1], row[2])


single_customer('Susan', '../data/test_items.csv')
