from unittest import TestCase
from unittest.mock import MagicMock

from inventory_management.inventoryClass import inventory
from inventory_management.furnitureClass import furniture
from inventory_management.electricAppliancesClass import electricAppliances
from inventory_management.market_prices import get_latest_price

class ModuleTests(TestCase):

    def test_module(self):
        productCode0 = "productCode0"
        description = "description"
        marketPrice = "marketPrice"
        rentalPrice = "rentalPrice"

        newItem0  = inventory(productCode0, description, marketPrice, rentalPrice)
        self.assertEqual(newItem0.returnAsDictionary()['productCode'], productCode0)

        productCode1 = "productCode1"
        material = "material"
        size = "size"

        newItem1  = furniture(productCode1, description, marketPrice, rentalPrice, material, size)
        self.assertEqual(newItem1.returnAsDictionary()['productCode'], productCode1)

        productCode2 = "productCode2"
        brand = "brand"
        voltage = "voltage"

        newItem2  = electricAppliances(productCode2, description, marketPrice, rentalPrice, brand, voltage)
        self.assertEqual(newItem2.returnAsDictionary()['productCode'], productCode2)