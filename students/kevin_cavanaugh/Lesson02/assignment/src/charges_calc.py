"""
Returns total price paid for individual rentals
"""
import argparse
import json
import datetime
import math
import logging

# formats logging output  & logfile name
log_format = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
log_file = datetime.datetime.now().strftime("%Y-%m-%d")+'_charges_calc.log'
formatter = logging.Formatter(log_format)


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
            data = json.load(file)
        except ValueError:
            exit(0)
    return data


def calculate_additional_fields(data):
    """
    calculates additional fields based on the load file
    """
    for value in data.values():
        try:
            rental_start = datetime.datetime.strptime(
                value['rental_start'], '%m/%d/%y')
            rental_end = datetime.datetime.strptime(
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
                logger.warning(
                    f"Item has no rental end "
                    f"date. {value['rental_end']}")
        except ZeroDivisionError:
            if value['units_rented'] == 0:
                logger.error(
                    f"No units rented, cannot calculate "
                    f"unit_cost. {value['units_rented']}")

    return data


def save_to_json(filename, data):
    """
    outputs newly created data to new file
    """
    with open(filename, 'w') as file:
        json.dump(data, file)


if __name__ == "__main__":
    args = parse_cmd_arguments()
    # set up file handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    # set up console handler
    console_handler = logging.StreamHandler(log_file)
    console_handler.setFormatter(formatter)

    logger = logging.getLogger()

    if args.debug == 0:
        logger.disabled = True
    elif args.debug == 1:
        file_handler.setLevel(logging.ERROR)
        console_handler.setLevel(logging.ERROR)
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    elif args.debug == 2:
        file_handler.setLevel(logging.WARNING)
        console_handler.setLevel(logging.WARNING)
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    elif args.debug == 3:
        file_handler.setLevel(logging.WARNING)
        console_handler.setLevel(logging.DEBUG)
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    data = load_rentals_file(args.input)
    data = calculate_additional_fields(data)
    save_to_json(args.output, data)
