'''
Returns total price paid for individual rentals 
'''
import argparse
import json
import datetime
import math
import logging

# format log
log_format = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
formatlog = logging.Formatter(log_format)

# create log output, set level, set format
file_handler = logging.FileHandler('charges_calc.log')
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(formatlog)

# set console handler
# add info to console as script runs
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# get 'root' logger
logger = logging.getLogger()
logger.setLevel(logging.WARNING)

# add multiple handlers
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# add our file_handler to the 'root' logger's handlers
logger.addHandler(file_handler)

def parse_cmd_arguments():
    '''This function will add arguments added from command line.'''
    try:
        parser = argparse.ArgumentParser(description=
                                         'Process some integers.')
        parser.add_argument('-i', '--input',
                            help='input JSON file', required=True)
        parser.add_argument('-o', '--output',
                            help='ouput JSON file', required=True)

        logging.debug("{} has been added successfully")

        return parser.parse_args()


    except TypeError:
        logging.warning("Add argument to parser failed. incorrect argument {}"
                        .format(parser.parse_args()))
    except ValueError:
        logging.warning("Add argument to parser failed. incorrect argument {}"
                        .format(parser.parse_args()))

def load_rentals_file(filename):
    '''This function will take all calculated data and add it
       to the specified args file'''
    with open(filename) as file:
        try:
            data = json.load(file)
        except ValueError:
            exit(0)
    return data

def calculate_additional_fields(data):
    '''Calculate the data from the input json file. '''
    for value in data.values():
        try:
            rental_start = datetime.datetime.strptime(value['rental_start'], '%m/%d/%y')
            rental_end = datetime.datetime.strptime(value['rental_end'], '%m/%d/%y')
            value['total_days'] = (rental_end - rental_start).days
            value['total_price'] = value['total_days'] * value['price_per_day']
            value['sqrt_total_price'] = math.sqrt(value['total_price'])
            value['unit_cost'] = value['total_price'] / value['units_rented']

            logging.debug("{} has been calculated. ".format(value['product_code']))


        except ValueError:
            logging.error("incorrect value for rental_start: {} or rental_end: {}"
                                .format(rental_start, rental_end))

            # separate text file added for more clarity on data issues
            with open('errordata.txt', 'a') as er:
                er.write(str(value))
                er.write('\n')

            # This command can be un-commented and will only capture data in
            # charges_calc.log that has a value error. Then the script will end.
            # exit(0)

        except:
            exit(0)

    return data

def save_to_json(filename, data):
    '''Save all data and dump it to the file. '''
    try:
        with open(filename, 'w') as file:
            json.dump(data, file)

    except ValueError:
        logging.error("data not saved to json output correctly.")


if __name__ == "__main__":
    args = parse_cmd_arguments()
    data = load_rentals_file(args.input)
    data = calculate_additional_fields(data)
    save_to_json(args.output, data)
