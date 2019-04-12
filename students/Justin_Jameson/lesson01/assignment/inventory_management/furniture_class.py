# Furniture class
from inventory_class import Inventory


class Furniture(Inventory):

    def __init__(self,
                 product_code,
                 description,
                 market_price,
                 rental_price,
                 material,
                 size):
        # Creates common instance variables from the parent class
        Inventory.__init__(self,
                           product_code,
                           description,
                           market_price,
                           rental_price)

        self.material = material
        self.size = size

    def return_as_dictionary(self):
        outputDict = {}
        outputDict['product_code'] = self.product_code
        outputDict['description'] = self.description
        outputDict['market_price'] = self.market_price
        outputDict['rental_price'] = self.rental_price
        outputDict['material'] = self.material
        outputDict['size'] = self.size

        return outputDict
