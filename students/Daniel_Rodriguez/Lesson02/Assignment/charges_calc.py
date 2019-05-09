"""
Returns total price paid for individual rentals
"""
import argparse
from argparse import RawTextHelpFormatter

import json
import datetime
import math
import logging

# logging.basicConfig(level=logging.DEBUG)


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


def load_rentals_file(filename):
    """
    load_rentals_file
    :param filename:
    :return:
    """
    logging.debug('Reading input JSON file')
    logging.debug('Inside load_rentals_file function')
    logging.debug('Opening Filename: {}'.format(filename))

    with open(filename) as file:
        try:
            data = json.load(file)
            logging.debug('Reading data file...')
        except Exception as error:
            logging.error('Source JSON file {} could not be loaded! '
                            .format(filename))
            logging.error('Error Message: {}'.format(error))
            exit(0)
    return data


def calculate_additional_fields(data):
    """
    calculate_additional_fields
    :param data:
    :return:
    """
    logging.debug('Calculating additional data fields')
    logging.debug('Inside calculate_additional_fields function')

    for key, value in data.items():

        logging.debug('Processing Rental Record: {}'.format(key))

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

            logging.debug('Total Days: {}'.format(value['total_days']))
            logging.debug('Total Price: {}'.format(value['total_price']))
            logging.debug('Total Square Root of Price: {:.2f}'
                          .format(value['sqrt_total_price']))
            logging.debug('Total Unit Costs: {:.2f}'.format(value['unit_cost']))

        except ValueError:
            logging.warning('Error Processing Rental Record: {}.'.format(key))
            logging.warning('Rental End Date {} before Start Date {}!'
                            .format(value['rental_end'], value['rental_start']))

    return data


def save_to_json(filename, data):
    """
    Save file
    :param filename:
    :param data:
    :return:
    """
    logging.debug('Saving data to output JSON file: {}'.format(filename))
    logging.debug('Inside save_to_json function')

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":

    args = parse_cmd_arguments()

    LOG_FORMAT = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s " \
                 "%(message)s"
    LOG_FILE = 'charges_calc.log'

    if args.debug == '1':
        LOGGING_LEVEL_FILE = 'ERROR'
        LOGGING_LEVEL_CONSOLE = 'ERROR'
    elif args.debug == '2':
        LOGGING_LEVEL_FILE = 'WARNING'
        LOGGING_LEVEL_CONSOLE = 'WARNING'
    elif args.debug == '3':
        LOGGING_LEVEL_FILE = 'WARNING'
        LOGGING_LEVEL_CONSOLE = 'DEBUG'
    else:
        LOGGING_LEVEL_FILE = 'NOTSET'
        LOGGING_LEVEL_CONSOLE = 'NOTSET'

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setLevel(LOGGING_LEVEL_FILE)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(LOGGING_LEVEL_CONSOLE)

    formatter = logging.Formatter(LOG_FORMAT)
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logging.debug('Calling load_rentals_file with argument {}'
                  .format(args.input))

    DATA = load_rentals_file(args.input)

    logging.debug('Calling calculate_additional_fields')
    DATA = calculate_additional_fields(DATA)

    logging.debug('Calling save_to_json')
    save_to_json(args.output, DATA)
