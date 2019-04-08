from unittest import TestCase
from inventory_management.inventory_class import Inventory
from inventory_management.electric_appliances_class import ElectricAppliances


class InventoryTests(TestCase):

    def test_return_as_dictionary(self):
        chair = Inventory(1, 'brown', 25, 30)

        test_dictionary = {
            'product_code': 1,
            'description': 'brown',
            'market_price': 25,
            'rental_price': 30
        }

        for key, value in test_dictionary.items():
            self.assertEqual(test_dictionary[f'{key}'],
                             chair.return_as_dictionary()[f'{key}'])

        self.assertEqual(dict, type(chair.return_as_dictionary()))


class ElectricAppliancesTests(TestCase):

    def test_return_as_dictionary(self):
        stove = ElectricAppliances(2, 'black', 200, 100, 'Steve Stoves', 55)

        test_dictionary = {
            'product_code': 2,
            'description': 'black',
            'market_price': 200,
            'rental_price': 100,
            'brand': 'Steve Stoves',
            'voltage': 55
        }

        for key, value in test_dictionary.items():
            self.assertEqual(test_dictionary[f'{key}'],
                             stove.return_as_dictionary()[f'{key}'])

        self.assertEqual(dict, type(stove.return_as_dictionary()))


if __name__ == '__main__':
    unittest.main()
