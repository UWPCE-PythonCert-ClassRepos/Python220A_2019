'''
Returns total price paid for individual rentals
based on input file
'''


import argparse
import json
import datetime
import math
import logging


def set_up_logger(debug):
    """
    Function to set up logger
    :return:
    """
    # Change Debugger Level to an Integer
    debug = int(debug)
    if debug is None:
        logging.debug("Warning, No Debugger Provided!")
    elif debug > 0:
        # Set Log Formatting Options
        log_format = "%(asctime)s %(filename)s:%(lineno)-4d %(levelname)s %(message)s"

        # Create formatter object
        formatter = logging.Formatter(log_format)

        # Set Log File Locations
        file_handler = logging.FileHandler('charges_calc.log')

        # Pass Formatter to file handler
        file_handler.setFormatter(formatter)

        # Create an instance of the Logger
        logger = logging.getLogger()
        # Pass File Handler to the logger
        logger.addHandler(file_handler)

        # Set the Debuggers Warning Level
        if debug == 1:
            logger.setLevel(logging.ERROR)
        elif debug == 2:
            logger.setLevel(logging.WARNING)
        else:
            logger.setLevel(logging.DEBUG)

def my_logger(orig_func):
    """
    Wrapper that togglers Logging
    :param orig_func: Original Functino to be decroated
    :return: Original Function w/ or w/o Logging
    """
    def wrapper(*args, **kwargs):
        # Case Statement to Turn on Logging
        if int(TOGGLE) == 0:
            logging.getLogger().disabled = True
            return orig_func(*args, **kwargs)
        # Case Statement to Turn Off Logging
        elif int(TOGGLE) != 0:
            logging.getLogger().disabled = False
            return orig_func(*args, **kwargs)
    return wrapper


def parse_cmd_arguments():
    """
    Function creates arguments at the command prompt
    :return: Command promp arguments
    """
    logging.debug("Inside parse_cmd_arguments")
    parser = argparse.ArgumentParser(description='Process some integers.')
    # add_argument specifies which command-line options the program is willing to accept
    parser.add_argument('-i', '--input', help='input JSON file', required=True)
    parser.add_argument('-o', '--output', help='ouput JSON file', required=True)
    # Add the Debugging Element to the Command Prompt
    parser.add_argument('-d', '--debugger', help='debugging Option', required=False, default=0)
    parser.add_argument('-l', '--logger', help='Toggle Logging', required=False, default=0)
    logging.debug("Arguments Correctly Parsed!")
    return parser.parse_args()

@my_logger
def load_rentals_file(filename):
    """
    Loads information from .json file
    :param filename: directory location of target file
    :return: De-coded .json Data
    """
    logging.debug("Inside load_rentals_file")
    with open(filename) as file:
        # Logging Statement to show that a file was made
        logging.debug("File Successfully Loaded in load_rentals_file")
        try:
            data = json.load(file)

        except:
            # Change to logging statement
            logging.warning("No Data Loaded in load_rentals_file")

    return data

@my_logger
def calculate_additional_fields(data):
    """
    Performs calculations based on provided input data
    :param data: Data to be analyzed
    :return: Data with additional information processing
    """

    logging.debug("Inside calculate_additional_fields")
    for value in data.values():

        try:
            rental_start = datetime.datetime.strptime(value['rental_start'], '%m/%d/%y')
            rental_end = datetime.datetime.strptime(value['rental_end'], '%m/%d/%y')
            # Provide a warning statement where there is no end date
            if rental_end is None:
                logging.warning("No Rental End Date Provided")
            value['total_days'] = (rental_end - rental_start).days
            value['total_price'] = value['total_days'] * value['price_per_day']
            value['sqrt_total_price'] = math.sqrt(value['total_price'])
            value['unit_cost'] = value['total_price'] / value['units_rented']
        except ValueError:
            logging.error("Error Occurred When Determining \
                          Square Root of Cost")
            value['sqrt_total_price'] = "Error"
        except ZeroDivisionError:
            logging.error("Zero Division Error!")

    return data

@my_logger
def save_to_json(filename, data):
    """
    Saves data to .json file
    :param filename: File path to save data
    :param data: information to save in .json file
    :return: Saves to directory
    """
    if filename is None:
        logging.warning("No Output File path Specified!")
    logging.debug("Inside save_to_json")
    with open(filename, 'w') as file:
        json.dump(data, file)
        logging.info("File Has Been Saved as {}".format(filename))


if __name__ == "__main__":
    ARGS = parse_cmd_arguments()
    # Create Statement to log where no logging occurs
    set_up_logger(ARGS.debugger)
    # Determine the Logging Toggler
    TOGGLE = ARGS.logger
    DATA = load_rentals_file(ARGS.input)
    DATA = calculate_additional_fields(DATA)
    save_to_json(ARGS.output, DATA)
