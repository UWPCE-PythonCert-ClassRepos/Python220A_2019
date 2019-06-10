#!/usr/bin/env python3
'''
Returns total price paid for individual rentals
'''
import argparse
import json
import datetime
import math
import logging

def setup_logger(level):
    """
    Sets up the logger if desired, or a dummy logger by default.
    """
    logger = logging.getLogger(__name__)
    # return the disabled logger if no logging requested
    if level is None:
        logger.disabled = True
        return logger
    log_format = " ".join(["%(asctime)s",
                           "%(filename)s:%(lineno)-3d",
                           "%(levelname)s %(message)s"])
    log_file = datetime.datetime.now().strftime("%Y-%m-%d")+'.log'
    formatter = logging.Formatter(log_format)
    logger.setLevel(level)
    file_level = logging.WARNING if level == logging.DEBUG else level
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(file_level)
    file_handler.setFormatter(formatter)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger

def parse_cmd_arguments():
    """
    Parses cli arguments
    """
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input', help='input JSON file', required=True)
    parser.add_argument('-o', '--output', help='ouput JSON file', required=True)
    parser.add_argument('-d',
                        '--debug',
                        help='Debug level: 0 (quietest) to 3 (most verbose)',
                        required=False)

    return parser.parse_args()

def loggerizer(func):
    """ Adds function start/stop logging if debugging is enabled """
    def log_all_the_things(*args):
        # Note that the original lesson02 instructions require that only
        # errors/warnings write to disk.  So this will only be seen on stderr
        LOGGER.info("Calling function %s().", func.__name__)
        # log all function arguments for DEBUG
        LOGGER.debug("Arguments to function %s(): %s.", func.__name__, args)
        data = func(*args)
        LOGGER.info("Ended function %s().", func.__name__)
        return data
    return log_all_the_things

@loggerizer
def load_rentals_file(filename):
    """
    Loads a json file
    """
    LOGGER.debug("load_rentals_file()")
    try:
        with open(filename) as file:
            LOGGER.debug("Loading JSON data from %s", filename)
            data = json.load(file)
            LOGGER.debug("Successfully loaded JSON data.")
    except Exception as err:
        LOGGER.error("Failed to load JSON data. %s", err)
        raise err
    return data

@loggerizer
def calculate_additional_fields(data):
    """
    Calculates additional fields
    """
    keys = ['rental_start', 'rental_end', 'price_per_day', 'units_rented']
    for value in data.values():
        missing_keys = [x for x in keys if not x in value.keys()]
        if missing_keys:
            LOGGER.warning("Could not find required key(s) %s in %s.  Skip.",
                           missing_keys,
                           value)
            continue
        try:
            rental_start = datetime.datetime.strptime(value['rental_start'],
                                                      '%m/%d/%y')
            rental_end = datetime.datetime.strptime(value['rental_end'],
                                                    '%m/%d/%y')
        except ValueError as err:
            LOGGER.warning("Failed to calculate time from %s or %s. %s",
                           value['rental_start'],
                           value['rental_end'],
                           err)
        if value['units_rented'] == 0:
            LOGGER.error("Units rented is 0 for %s.  Skip.", value)
            continue
        if rental_start >= rental_end:
            LOGGER.warning("Rental start %s on or after end %s in %s.  Skip.",
                           rental_start,
                           rental_end,
                           value)
            continue
        try:
            value['total_days'] = (rental_end - rental_start).days
            value['total_price'] = value['total_days'] * value['price_per_day']
            value['sqrt_total_price'] = math.sqrt(value['total_price'])
            value['unit_cost'] = value['total_price'] / value['units_rented']
        except Exception as err:
            LOGGER.error("Failed to calculate fields for %s. %s", value, err)
            raise err

    return data

@loggerizer
def save_to_json(filename, data):
    """
    Saves data in JSON format to a file
    """
    try:
        with open(filename, 'w') as file:
            json.dump(data, file)
    except Exception as err:
        LOGGER.error("Failed to write output to %s. %s", filename, err)
        raise err

LOG_MAP = {'1': logging.ERROR,   # errors
           '2': logging.WARNING, # errors and warnings
           '3': logging.DEBUG}   # errors, warnings, and debug

if __name__ == "__main__":
    ARGS = parse_cmd_arguments()
    if ARGS.debug and ARGS.debug in LOG_MAP:
        LOGGER = setup_logger(LOG_MAP[ARGS.debug])
    else:
        LOGGER = setup_logger(None)
    LOGGER.debug("Logging initialized")
    DATA = load_rentals_file(ARGS.input)
    DATA = calculate_additional_fields(DATA)
    save_to_json(ARGS.output, DATA)
