"""
Returns total price paid for individual rentals
"""
import argparse
import json
import datetime
import math
import logging
import logging.config


def init_logging(logging_level):
    """ Setting up the logger
    lvl 1 = only show error msgs on console and in file
    lvl 2 = only show error and warnings on console and in file
    lvl 3 = show all msgs on console and in file
    lvl 0 = show nothing and output nothing
    """
    logger = logging.getLogger(__name__)
    log_format = (
        "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s")
    log_file = datetime.datetime.now().strftime("%Y-%m-%d")+'.log'
    formatter = logging.Formatter(log_format)
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    if logging_level == 0:
        logger.disabled = True
    elif logging_level == 1:
        file_handler.setLevel(logging.ERROR)
        stream_handler.setLevel(logging.ERROR)
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)
    elif logging_level == 2:
        file_handler.setLevel(logging.WARNING)
        stream_handler.setLevel(logging.WARNING)
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)
    elif logging_level == 3:
        logging.config.fileConfig(
            fname='logging.conf', disable_existing_loggers=False)

    return logger


def parse_cmd_arguments():
    """ Parse arguments from cmdline """
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i',
                        '--input',
                        help='input JSON file',
                        required=True)
    parser.add_argument('-o',
                        '--output',
                        help='ouput JSON file',
                        required=True)
    parser.add_argument('-d',
                        '--debug',
                        type=int,
                        choices=[0, 1, 2, 3],
                        help='logging debug lvl> 1: error, 2: warn, 3: debug',
                        default=0,
                        required=False)

    return parser.parse_args()


def load_rentals_file(filename):
    """ Load JSON rental file """
    LOGGER.debug("Loading JSON file %s", filename)
    with open(filename) as file:
        try:
            data = json.load(file)
        except ValueError:
            exit(0)
    return data


def calculate_additional_fields(data):
    """ Calculate various values and return data dict """
    for key, value in list(data.items()):
        try:
            LOGGER.debug("Current item: %s", value)
            rental_start = datetime.datetime.strptime(
                value['rental_start'], '%m/%d/%y')
            rental_end = datetime.datetime.strptime(
                value['rental_end'], '%m/%d/%y')
            # Removing key from output since it will return incorrect data
            if rental_start > rental_end:
                LOGGER.error(
                    "Rental start date is after rental end date. %s", key)
                del data[key]
            elif rental_start == rental_end:
                LOGGER.warning(
                    "Rental was returned the same day. %s", key)
            else:
                value['total_days'] = (rental_end - rental_start).days
                value['total_price'] = (
                    value['total_days'] * value['price_per_day'])
                value['sqrt_total_price'] = math.sqrt(value['total_price'])
                value['unit_cost'] = (
                    value['total_price'] / value['units_rented'])
                LOGGER.debug("Current item after changes: %s", value)
        except ValueError as value_error:
            if value['rental_end'] == "":
                LOGGER.warning(
                    "Item has no rental end date. Msg: %s", value_error)
        except ZeroDivisionError as division_error:
            if value['units_rented'] == 0:
                LOGGER.error(
                    "No units rented, can't calculate unit_cost. Msg: %s",
                    division_error)
    return data


def save_to_json(filename, data):
    """ Save data to JSON file """
    with open(filename, 'w') as file:
        json.dump(data, file)

if __name__ == "__main__":
    ARGS = parse_cmd_arguments()
    LOGGER = init_logging(ARGS.debug)
    LOGGER.debug("ARGS passed into the script, %s", ARGS)
    DATA = load_rentals_file(ARGS.input)
    DATA = calculate_additional_fields(DATA)
    save_to_json(ARGS.output, DATA)
