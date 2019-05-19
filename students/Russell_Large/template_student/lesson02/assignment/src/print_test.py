# Testing output values

import datetime
import math

tst = {"RNT001": {
    "product_code": "PRD80",
    "units_rented": 8,
    "price_per_day": 31,
    "rental_start": "6/12/17",
    "rental_end": "3/22/17"
  }}

for value in tst.values():

    rental_start = datetime.datetime.strptime(value['rental_start'], '%m/%d/%y')
    print(rental_start)
    rental_end = datetime.datetime.strptime(value['rental_end'], '%m/%d/%y')
    print(rental_end)
    value['total_days'] = (rental_end - rental_start).days
    print("total_days: {}".format(value['total_days']))
    value['total_price'] = value['total_days'] * value['price_per_day']
    print("total_price: {}".format(value['total_price']))
    value['sqrt_total_price'] = math.sqrt(value['total_price'])
    print("sqrt_total_price: {}".format(value['sqrt_total_price']))
    value['unit_cost'] = value['total_price'] / value['units_rented']
    print(value['unit_cost'])
    value['unit_cost'] = value['total_price'] / value['units_rented']

