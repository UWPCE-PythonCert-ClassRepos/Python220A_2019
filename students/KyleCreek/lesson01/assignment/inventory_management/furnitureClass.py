""" This Module Establishes the Furniture Class """
from inventory_management.InventoryClass import Inventory


class Furniture(Inventory):
    """
    Represents the Furniture Class of the inventory Object
    """

    def __init__(self, product_code, description, market_price,
                 rental_price, material, size):
        # Creates common instance variables from the parent class
        Inventory.__init__(self, product_code,
                           description, market_price, rental_price)

        self.material = material
        self.size = size

    def return_as_dictionary(self):
        """
        Returns Class Representation as a Dictionary
        :return: Dictionary Representation of the Electric Appliance
        class
        """

        output_dict = super(Furniture, self).return_as_dictionary()
        output_dict['material'] = self.material
        output_dict['size'] = self.size

        return output_dict
