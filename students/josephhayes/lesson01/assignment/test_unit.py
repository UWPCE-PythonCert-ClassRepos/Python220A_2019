from unittest import TestCase
from unittest.mock import MagicMock

from inventory_management.inventoryClass import inventory
from inventory_management.furnitureClass import furniture
from inventory_management.electricAppliancesClass import electricAppliances
from inventory_management.market_prices import get_latest_price


class InventoryClassTests(TestCase):

    def test_inventory_creation(self):
        productCode = "productCode"
        description = "description"
        marketPrice = "marketPrice"
        rentalPrice = "rentalPrice"

        newItem  = inventory(productCode, description, marketPrice, rentalPrice)
        itemDict = newItem.returnAsDictionary()
        self.assertEqual(itemDict['productCode'], productCode)
        self.assertEqual(itemDict['description'], description)
        self.assertEqual(itemDict['marketPrice'], marketPrice)
        get_latest_price = MagicMock(return_value=24)
        get_latest_price(productCode)
        get_latest_price.assert_called_with(productCode)

class FurnitureClassTests(TestCase):

    def test_furniture_creation(self):
        productCode = "productCode"
        description = "description"
        marketPrice = "marketPrice"
        rentalPrice = "rentalPrice"
        material = "material"
        size = "size"

        newItem  = furniture(productCode, description, marketPrice, rentalPrice, material, size)
        itemDict = newItem.returnAsDictionary()
        self.assertEqual(itemDict['productCode'], productCode)
        self.assertEqual(itemDict['description'], description)
        self.assertEqual(itemDict['marketPrice'], marketPrice)
        self.assertEqual(itemDict['rentalPrice'], rentalPrice)
        self.assertEqual(itemDict['material'], material)
        self.assertEqual(itemDict['size'], size)

class ElectricAppliancesTests(TestCase):
    """ tests the electricAppliances class"""

    def test_appliances_creation(self):
        productCode = "productCode"
        description = "description"
        marketPrice = "marketPrice"
        rentalPrice = "rentalPrice"
        brand = "brand"
        voltage = "voltage"

        newItem  = electricAppliances(productCode, description, marketPrice, rentalPrice, brand, voltage)
        itemDict = newItem.returnAsDictionary()
        self.assertEqual(itemDict['productCode'], productCode)
        self.assertEqual(itemDict['description'], description)
        self.assertEqual(itemDict['marketPrice'], marketPrice)
        self.assertEqual(itemDict['rentalPrice'], rentalPrice)
        self.assertEqual(itemDict['brand'], brand)
        self.assertEqual(itemDict['voltage'], voltage)

if __name__ == "__main__":
    tests = InventoryClassTests()
    tests.test_inventory_creation()
    tests = FurnitureClassTests()
    tests.furniture()
    tests = ElectricAppliancesTests()
    tests.test_appliances_creation()