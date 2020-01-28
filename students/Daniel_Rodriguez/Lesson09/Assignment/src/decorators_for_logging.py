# Title: Test Using Decorators for Logging
# Date: 6/3/2019
# Author: Daniel A. Rodriguez-Delgado (1701667)
# Revision Record: (Date, Revision, Author)
# 
# No DB

import json
import datetime
import math
import argparse
from argparse import RawTextHelpFormatter


# Define logger decorator function
def logger_decorator(original_function):
    import logging
    # logging.basicConfig(filename='{}.log'.format(original_function.__name__),
    #                     level=logging.INFO)

    # log_format = "%(asctime)s %(filename)s:%(lineno)-4d %(levelname)s %(message)s"

    log_format = "%(asctime)s:%(lineno)-4d %(levelname)s %(message)s"
    file_name = 'test_log.log'
    logging.basicConfig(level=logging.DEBUG, format=log_format,
                        filename=file_name)

    def wrapper(*args, **kwargs):
        logging.info(
            'Ran {} with args: {}, and kwargs {}'.format(
                original_function.__name__, args, kwargs))
        return original_function(*args, **kwargs)

    return wrapper


@logger_decorator
def parse_cmd_arguments():
    """
    Parse command line arguments
    :return:
    """
    parser = argparse.ArgumentParser(description='Process some integers.',
                                     formatter_class=RawTextHelpFormatter)

    parser.add_argument('-i', '--input', help='Input JSON file', required=True)
    parser.add_argument('-o', '--output', help='Output JSON file',
                        required=True)

    parser.add_argument('-d', '--debug', help='Debug message level:\n'
                                              '0: No debug messages or '
                                              'log file\n'
                                              '1: Only error messages\n'
                                              '2: Error messages and warnings\n'
                                              '3: Error messages, warnings,'
                                              'and debug messages',
                        required=False)

    return parser.parse_args()


@logger_decorator
def load_rentals_file(filename):
    """
    load_rentals_file
    :param filename:
    :return:
    """

    with open(filename) as file:
        try:
            data = json.load(file)
            # logging.debug('Reading data file...')
        except Exception as error:
            # logging.error('Source JSON file {} could not be loaded! '
            #                 .format(filename))
            # logging.error('Error Message: {}'.format(error))
            exit(0)
    return data


@logger_decorator
def calculate_additional_fields(data):
    """
    calculate_additional_fields
    :param data:
    :return:
    """

    for key, value in data.items():

        try:
            rental_start = datetime.datetime.strptime(
                value['rental_start'], '%m/%d/%y')

            rental_end = datetime.datetime.strptime(
                value['rental_end'], '%m/%d/%y')

            # Add new calculated values to data
            value['total_days'] = (rental_end - rental_start).days
            value['total_price'] = value['total_days'] * value['price_per_day']
            value['sqrt_total_price'] = math.sqrt(value['total_price'])
            value['unit_cost'] = value['total_price'] / value['units_rented']

        except ValueError:
            pass
            # logging.warning('Error Processing Rental Record: {}.'.format(key))
            # logging.warning('Rental End Date {} before Start Date {}!'
            #                 .format(value['rental_end'], value['rental_start']))

    return data


@logger_decorator
def save_to_json(filename, data):
    """
    Save file
    :param filename:
    :param data:
    :return:
    """

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == '__main__':
    args = parse_cmd_arguments()

    DATA = load_rentals_file(args.input)

    DATA = calculate_additional_fields(DATA)

    save_to_json(args.output, DATA)
