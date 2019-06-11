import csv
import os
from functools import partial


def add_furniture(invoice_file, customer_name, item_code, item_description,
                  item_monthly_price):
    """
    add furniture invoice info to csv
    """
    if os.path.isfile(invoice_file):
        with open(invoice_file, 'a+') as file:
            writer = csv.DictWriter(file,
                                    lineterminator='\n',
                                    fieldnames=["Customer_Name",
                                                "Item_Code",
                                                "Item_Description",
                                                "Monthly_Price"])
            writer.writerow(dict(
                Customer_Name=customer_name,
                Item_Code=item_code,
                Item_Description=item_description,
                Monthly_Price=item_monthly_price))
    else:
        with open(invoice_file, 'w+') as file:
            writer = csv.DictWriter(file,
                                    lineterminator='\n',
                                    fieldnames=["Customer_Name",
                                                "Item_Code",
                                                "Item_Description",
                                                "Monthly_Price"])
            writer.writerow(dict(
                Customer_Name=customer_name,
                Item_Code=item_code,
                Item_Description=item_description,
                Monthly_Price=item_monthly_price))


def single_customer(customer_name, invoice_file):
    add = partial(add_furniture,
                  customer_name=customer_name,
                  invoice_file=invoice_file)

    def create_invoice(rental_items):
        with open(rental_items, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                add(item_code=row[0],
                    item_description=row[1],
                    item_monthly_price=row[2])
        return add
    return create_invoice


def main():
    """
    main
    """
    # add_furniture('invoice.csv', 'Elisa Miles', 'LR04',
    #               'Leather Sofa', '25.00')
    # add_furniture('invoice.csv', 'Edward Data', 'KT78',
    #               'Kitchen Table', '10.00')
    # add_furniture('invoice.csv', 'Alex Gonzales', 'BR02',
    #               'Queen Mattress', '17.00')
    dan_invoice = single_customer(r'Dan C',
                                  r'C:\Python220\Python220A_2019\students\kevin_cavanaugh\lesson08\assignment\src\invoice.csv')
    dan_invoice(r'C:\Python220\Python220A_2019\students\kevin_cavanaugh\lesson08\assignment\data\test_items.csv')


if __name__ == '__main__':
    main()
