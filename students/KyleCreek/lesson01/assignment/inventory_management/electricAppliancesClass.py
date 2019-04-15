""" This module Establishes the Electric Appliances Class """
from inventory_management.InventoryClass import Inventory


class ElectricAppliances(Inventory):
    """
    Class to represent electric Appliance. Sub-Class of the inventory
    object
    """

    # Creates common instance variables from the parent class
    def __init__(self, product_code, description, market_price,
                 rental_price, brand, voltage):
        Inventory.__init__(self, product_code, description,
                           market_price, rental_price)
        self.brand = brand
        self.voltage = voltage

    def return_as_dictionary(self):
        """
        Returns Class Representation as a Dictionary
        :return: Dictionary Representation of the Electric Appliance
        class
        """

        output_dict = super(ElectricAppliances, self).return_as_dictionary()
        output_dict['brand'] = self.brand
        output_dict['voltage'] = self.voltage

        return output_dict
