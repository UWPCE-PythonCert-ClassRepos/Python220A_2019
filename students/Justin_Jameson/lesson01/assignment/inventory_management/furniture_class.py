# Furniture class
""" Fixing docstring """
from inventory_class import Inventory


class Furniture(Inventory):
    """ creating a child class of Inventory"""
    def __init__(self,
                 product_code,
                 description,
                 market_price,
                 rental_price,
                 material,
                 size):
        """Creates common instance variables from the parent class"""
        Inventory.__init__(self,
                           product_code,
                           description,
                           market_price,
                           rental_price)

        self.material = material
        self.size = size
        self.output_dict = {}

    def return_as_dictionary(self):
        """"can I get rid of the replicated ones from the original class?"""
        #  output_dict = {}
        self.output_dict['product_code'] = self.product_code
        self.output_dict['description'] = self.description
        self.output_dict['market_price'] = self.market_price
        self.output_dict['rental_price'] = self.rental_price
        self.output_dict['material'] = self.material
        self.output_dict['size'] = self.size

        return self.output_dict
