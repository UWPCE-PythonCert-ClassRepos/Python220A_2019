from unittest import TestCase
from unittest.mock import MagicMock

from InventoryClass import Inventory
from ElectricAppliancesClass import ElectricAppliances
from FurnitureClass import Furniture
from main import *


class InventoryTests(TestCase):
    def test_init(self):
        item = Inventory(1, "Item1", "200", "400")
        self.assertEqual(1, item.product_code)
        self.assertEqual("Item1", item.description)
        self.assertEqual("200", item.market_price)
        self.assertEqual("400", item.rental_price)


class ElectricAppliancesTests(TestCase):
    def test_init(self):
        item = ElectricAppliances(
            1,
            "EA1",
            "1000",
            "2000",
            brand="GE",
            voltage="220")
        self.assertEqual("220", item.voltage)
        self.assertEqual("GE", item.brand)
        self.assertEqual("EA1", item.description)


class FurnitureTests(TestCase):
    def test_init(self):
        item = Furniture(
            1,
            "F1",
            "5000",
            "6000",
            material="Leather",
            size="L")
        self.assertEqual("Leather", item.material)
        self.assertEqual("L", item.size)
        self.assertEqual("F1", item.description)


class MainTests(TestCase):
    pass


# if __name__ == '__main__' and __package__ is None:
#     from os import sys, path
#     sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
