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

    def returnasdictionary(self):
        """"fixing docstring"""
        outputDict = {}
        outputDict['product_code'] = self.product_code
        outputDict['description'] = self.description
        outputDict['market_price'] = self.market_price
        outputDict['rental_price'] = self.rental_price
        outputDict['brand'] = self.brand
        outputDict['voltage'] = self.voltage

        return outputDict
