# Electric appliances class
"""
This module provides methods to interact with the ElectricAppliances class
"""
from inventory_management.InventoryClass import Inventory


class ElectricAppliances(Inventory):
    """
    ElectricAppliances class to interact with electric appliance items
    """
    def __init__(
            self,
            *args,
            brand,
            voltage):

        super().__init__(*args)

        self.brand = brand
        self.voltage = voltage

    def return_as_dictionary(self):
        """
        Return the ElectricAppliances object as a dict
        """
        output_dict = {}
        output_dict = super(ElectricAppliances, self).return_as_dictionary()
        output_dict['brand'] = self.brand
        output_dict['voltage'] = self.voltage

        return output_dict
