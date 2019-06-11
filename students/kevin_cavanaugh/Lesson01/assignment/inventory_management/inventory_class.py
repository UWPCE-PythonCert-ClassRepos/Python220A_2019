'''
Inventory class
'''


class Inventory:
    '''
    class for creating inventory objects
    '''

    def __init__(self, product_code, description,
                 market_price, rental_price):
        '''
        construct inventory object
        :param product_code:
        :param description:
        :param market_price:
        :param rental_price:
        '''
        self.product_code = product_code
        self.description = description
        self.market_price = market_price
        self.rental_price = rental_price

    def return_as_dictionary(self):
        '''
        return inventory object as a dictionary
        :return:
        '''
        output_dict = {
            'product_code': self.product_code,
            'description': self.description,
            'market_price': self.market_price,
            'rental_price': self.rental_price
        }

        return output_dict
