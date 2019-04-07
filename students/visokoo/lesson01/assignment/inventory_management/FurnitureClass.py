# Furniture class
"""
This module provides methods to interact with the Furniture class
"""
from InventoryClass import Inventory


class Furniture(Inventory):
    """
    Furniture class to interact with furniture items
    """

    def __init__(
            self,
            *args,
            material,
            size):

        super().__init__(*args)

        self.material = material
        self.size = size

    def return_as_dictionary(self):
        """
        Return the Furniture object as a dict.
        """
        output_dict = {}
        output_dict = super(Furniture, self).return_as_dictionary()
        output_dict['material'] = self.material
        output_dict['size'] = self.size

        return output_dict
