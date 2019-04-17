from unittest import TestCase
from unittest.mock import MagicMock

from inventory_management.inventory_class import Inventory

class InventoryTests(TestCase):

    def test_return_as_dictionary(self):
        desk = Inventory(1, 'desk', 60, 80)

        self.assertEqual(dict, type(desk.return_as_dictionary()))


if __name__ == '__main__':
    unittest.main()
