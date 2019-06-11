"""
for assignment9
update assignment2
"""
import argparse
import json
from datetime import datetime
import math
import logging


def conditional_logger(func):
    """
    create a conditional logging decorator
    """
    def init_logging(logging_level,*args):
        """
        create logger with command line options
        :return: logger
        """
        logger = logging.getLogger(__name__)
        log_format = ('%(asctime)s '
                      '%(filename)s:'
                      '%(lineno)-3d '
                      '%(levelname)s '
                      '%(''messages)s')
        formatter = logging.Formatter(log_format)
        log_file = datetime.now().strftime('%Y-%m-%d') + '_charges_calc.log'
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        if logging_level == 0:
            logger.disabled = True
        elif logging_level == 1:
            file_handler.setLevel(logging.ERROR)
            logger.addHandler(file_handler)
            console_handler.setLevel(logging.ERROR)
            logger.addHandler(console_handler)
        elif logging_level == 2:
            file_handler.setLevel(logging.WARNING)
            logger.addHandler(file_handler)
            console_handler.setLevel(logging.WARNING)
            logger.addHandler(console_handler)
        elif logging_level == 3:
            file_handler.setLevel(logging.DEBUG)
            logger.addHandler(file_handler)
            console_handler.setLevel(logging.WARNING)
            logger.addHandler(console_handler)
        return func(*args)
    return init_logging


def parse_cmd_arguments():
    """
    passes in input, output and debugger level from the command line
    """
    parser = argparse.ArgumentParser(
        description='Process some integers.')
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
                        help='choose logging debug level:'
                             '1: error, 2: warn, 3: debug',
                        default=0,
                        required=False)

    return parser.parse_args()


def load_rentals_file(filename):
    """
    reads rental file
    """
    with open(filename) as file:
        try:
            json_data = json.load(file)
        except ValueError:
            exit(0)
    return json_data


@conditional_logger
def calculate_additional_fields(json_data):
    """
    calculates additional fields based on the load file
    """
    for value in json_data.values():
        try:
            rental_start = datetime.strptime(
                value['rental_start'], '%m/%d/%y')
            rental_end = datetime.strptime(
                value['rental_end'], '%m/%d/%y')
            if rental_end < rental_start:
                logging.error(f"End date,{value['rental_end']}, before, "
                              f"start date,{value['rental_start']}.")
                del value['rental_start']
            elif rental_end == rental_start:
                logging.warning(f"Same day return, "
                                f"{value['rental_start']}.")
            else:
                value['total_days'] = (rental_end - rental_start).days
                value['total_price'] = (value['total_days']
                                        * value['price_per_day'])
                value['sqrt_total_price'] = math.sqrt(value['total_price'])
                value['unit_cost'] = (
                    value['total_price'] / value['units_rented'])
        except ValueError:
            if value['rental_end'] == "":
                logging.warning(
                    f"Item has no rental end "
                    f"date. {value['rental_end']}")
        except ZeroDivisionError:
            if value['units_rented'] == 0:
                logging.error(
                    f"No units rented, cannot calculate "
                    f"unit_cost. {value['units_rented']}")

    return json_data


def save_to_json(filename, json_data):
    """
    outputs newly created data to new file
    """
    with open(filename, 'w') as file:
        json.dump(json_data, file)


if __name__ == "__main__":
    ARGS = parse_cmd_arguments()
    DATA = load_rentals_file(ARGS.input)
    DATA = calculate_additional_fields(ARGS.debug, DATA)
    save_to_json(ARGS.output, DATA)
