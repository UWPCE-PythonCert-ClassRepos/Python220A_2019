# Electric appliances class
"""
This files is a class for Electric appliances
"""
from inventory_class import Inventory


class ElectricAppliances(Inventory):
    """
    This class is for appliances.
    """
    def __init__(self,
                 product_code,
                 description,
                 market_price,
                 rental_price,
                 brand,
                 voltage):

        """Creates common instance variables from the parent class"""
        Inventory.__init__(self,
                           product_code,
                           description,
                           market_price,
                           rental_price)

        self.brand = brand
        self.voltage = voltage
        self.output_dict = {}

    def returnasdictionary(self):
        """"fixing docstring"""
        # output_dict = {}
        self.output_dict['product_code'] = self.product_code
        self.output_dict['description'] = self.description
        self.output_dict['market_price'] = self.market_price
        self.output_dict['rental_price'] = self.rental_price
        self.output_dict['brand'] = self.brand
        self.output_dict['voltage'] = self.voltage

        return self.output_dict
