# Inventory class
class Inventory:

    def __init__(self,
                 product_code,
                 description,
                 market_price,
                 rental_price):
        self.product_code = product_code
        self.description = description
        self.market_price = market_price
        self.rental_price = rental_price

    def return_as_dictionary(self):
        outputDict = {}
        outputDict['product_code'] = self.product_code
        outputDict['description'] = self.description
        outputDict['market_price'] = self.market_price
        outputDict['rental_price'] = self.rental_price

        return outputDict
