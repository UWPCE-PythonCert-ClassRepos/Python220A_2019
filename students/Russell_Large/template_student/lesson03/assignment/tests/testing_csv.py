import csv
import logging
import sys
import os
import datetime
import time
from timeit import default_timer as timer

# dynamically connect to the database
# as long as data, src, and tests are all located
# in the same directory.
db_folder = os.getcwd()
db_location = str(db_folder[:-6] + '\src')
sys.path.append(db_location)
input_data = str(db_folder[:-6] + '\data\customer.csv')
print(input_data)



# from customers_db_schema import *
# import basic_operations as l
#
#
#
# with open(data_source) as f:
#     while True:
#         try:
#             # data_source = [tuple(line) for line in csv.reader(f)]
#             # data_setup = iter(data_source)
#             # iteration = next(data_setup)
#             # print(iteration)
#             # yield iteration
#
#             value = next(csv.reader(f))
#         except StopIteration as s:
#             print(s)
#             break
#
# def load_customer_data(data_source):
#
#     with open(data_source) as f:
#         while True:
#             try:
#                 value = next(csv.reader(f))
#                 yield tuple(value)
#
#             except StopIteration as s:
#                 print(s)
#                 break
#
#                 #logger.info("interation is complete.")
#
# test = load_customer_data(r'C:\Python220\lesson03_new\fromwork\assignment\data\customer.csv')
#
# for customer in test:
#     l.add_customer(customer[0],
#                    customer[1],
#                    customer[2],
#                    customer[3],
#                    customer[4],
#                    customer[5],
#                    customer[6],
#                    customer[7]
#                    )

