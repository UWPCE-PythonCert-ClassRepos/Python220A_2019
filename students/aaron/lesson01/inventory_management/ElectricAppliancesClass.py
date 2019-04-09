"""
Electric appliances module
"""

from InventoryClass import Inventory

class ElectricAppliances(Inventory):
    """
    The electric appliances class
    """

    def __init__(self, product_code, description, market_price,
                 rental_price, brand, voltage):
        """
        Constructor for electricappliances
        """

        # Creates common instance variables from the parent class
        Inventory.__init__(self, product_code, description, market_price,
                           rental_price)

        self.brand = brand
        self.voltage = voltage

    def return_as_dictionary(self):
        """
        Returns a dictionary
        """
        output_dict = super().return_as_dictionary()
        output_dict['brand'] = self.brand
        output_dict['voltage'] = self.voltage

        return output_dict
