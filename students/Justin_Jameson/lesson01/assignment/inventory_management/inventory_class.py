# -------------------------------------------------#
# # Title:inventory class module for Inventory Management
# # Dev:   unknown
# # Date:  4/16/2019
# # ChangeLog: (Who, , What)
# Justin Jameson
# added content to doc strings
# -------------------------------------------------#

""" Super class for Inventory Management program """


class Inventory:
    """ Inventory class defining attributes, content
    is fed to this class from main.py and converted
    to a dictionary. """
    def __init__(self,
                 product_code,
                 description,
                 market_price,
                 rental_price):
        """ prepping input from main to place in dictionary"""
        self.product_code = product_code
        self.description = description
        self.market_price = market_price
        self.rental_price = rental_price

    def return_as_dictionary(self):
        """ Fixing doc string """
        output_dict = {}
        output_dict['product_code'] = self.product_code
        output_dict['description'] = self.description
        output_dict['market_price'] = self.market_price
        output_dict['rental_price'] = self.rental_price

        return output_dict
