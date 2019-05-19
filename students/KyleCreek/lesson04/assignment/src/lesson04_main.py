"""
# Title: lesson04_main.py
# Desc: Utilizes customer data to perform actions
# Change Log: (Who, When, What)
# KCreek, 4/27/2019, Created Script
"""
import csv
import os.path
import basic_operations
import logging
import random


def check_database():
    """
    Verifies existence of database
    :return: None
    """
    # Check for database existence
    if os.path.exists("lesson04.db"):
        pass
    else:
        logging.warning("lesson04.db Does not exist!")


def random_customer_viewer(filepath):
    """
    Generate a Random Customer ID from existing table for
    proof of concept
    :param filepath: File path containing .csv file
    :return: dictionary of random customer in database
    """
    # Store Customer ID Data  from csv into list
    with open(filepath, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader, None)
        csv_cust_id = []
        for row in csv_reader:
            csv_cust_id.append(row[0])

    # Pick a random Customer ID to search for
    rand_cust_int = random.randint(0, len(csv_cust_id))
    return_dict_test = basic_operations.search_customer(csv_cust_id[rand_cust_int])

    return return_dict_test


def file_reader(filepath=None):
    """
    Reads the .csv required for lesson04
    :param file: File Path containing data
    :return: None
    """
    if filepath is None:
        print("No File Path Provided")
    else:
        with open(filepath, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            # Call Next Statement to Skip the headers in the File
            next(csv_reader, None)
            # Take each row and add each of the customers
            for row in csv_reader:
                basic_operations.add_customer(*row)

#filepath = "C:\\Python220A_2019\\students\\KyleCreek\\lesson04\\assignment\\data\\customer.csv"
