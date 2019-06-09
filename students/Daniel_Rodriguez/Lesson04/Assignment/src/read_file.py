# ---------------------------------------------------------------------------- #
# Course: PYTHON 220: Advanced Programming in Python
# Script Title: Read CSV File
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-05-13, Initial release
# ---------------------------------------------------------------------------- #

import csv


with open('customer.csv') as csvfile:
    customer_data = csv.reader(csvfile, delimiter=',')
    for row in customer_data:
        print(row)
        # print(row[0])
        # print(row[0], row[1], row[2],)
