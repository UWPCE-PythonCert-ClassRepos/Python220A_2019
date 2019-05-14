# -------------------------------------------------#
# # Title: charges calculator for Inventory management.
# # Dev:   unknown
# # Date:  4/17/2019
# # ChangeLog: (Who, What)
# Justin Jameson
# correct ouput to output line 20 'ouptu JSON file'
# in source.json removed extra comma on line 5884 from
# 'units_rented': 7,,
# imported logger
# #-------------------------------------------------#

""" Returns total price paid for individual rentals """

import argparse
import json
import datetime
import math
import logging
logging.basicConfig(filename='charges_calc.log', level=logging.DEBUG)
log_format = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
formatter = logging.Formatter(log_format)
file_handler = logging.FileHandler('charges_calc.log')
file_handler.setFormatter(formatter)
logger = logging.getLogger()
logger.addHandler(file_handler)



def parse_cmd_arguments():
    logging.debug('called parse_cmd')
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input', help='input JSON file', required=True)
    parser.add_argument('-o', '--output', help='output JSON file', required=True)
    logging.debug('about to return parser.parse_arg')
    return parser.parse_args()


def load_rentals_file(filename):
    with open(filename) as file:
        try:
            logging.debug('you made it to the try except block')
            data = json.load(file)
        except:
            logging.warning('load_rentals_files threw an exception')
            exit(0)
    logging.debug('made it through try except about to "return data"')
    return data


def calculate_additional_fields(data):
    for value in data.values():
        logging.debug('trying to print values in data', value)
        try:
            logging.debug('cycling through calculate_add.. try block')
            rental_start = datetime.datetime.strptime(value['rental_start'], '%m/%d/%y')
            logging.debug('made it through rental_start')
            rental_end = datetime.datetime.strptime(value['rental_end'], '%m/%d/%y')
            logging.debug('made it through rental_end')
            value['total_days'] = (rental_end - rental_start).days
            logging.debug('made it through value total_days')
            value['total_price'] = value['total_days'] * value['price_per_day']
            logging.debug('made it through total_price')
            # value['sqrt_total_price'] = math.sqrt(value['total_price'])
            # logging.debug('made it through sqrt_total_price')
            value['unit_cost'] = value['total_price'] / value['units_rented']
            logging.debug('made it through calculate_add... try block', value)
        except:
            logging.warning('except block of calculate_add... this will exit the program without')
            exit(0)    
    logging.debug('about to return data from calculate_add...')
    return data


def save_to_json(filename, data):
    logging.debug('made it to "save_to_json')
    with open(filename, 'w') as file:
        json.dump(data, file)


if __name__ == "__main__":
    args = parse_cmd_arguments()
    logging.debug('stepping into data')
    data = load_rentals_file(args.input)
    logging.debug('returning data, now redefining data to calculate_add...')
    data = calculate_additional_fields(data)
    logging.debug('returned data from calculate_add..., now stepping into save_to_json')
    save_to_json(args.output, data)
