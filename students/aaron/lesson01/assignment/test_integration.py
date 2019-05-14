import sys
sys.path.append("inventory_management")

from unittest import TestCase
from unittest.mock import MagicMock, patch

from inventory_management.InventoryClass import Inventory
from inventory_management.ElectricAppliancesClass import ElectricAppliances
from inventory_management.FurnitureClass import Furniture
from inventory_management import main
from inventory_management import market_prices

class IntegrationTests(TestCase):
    def test_all_the_things(self):
        input_vars = [
                         "1", "1", "Socks", "100", "n", "n", "", "1", "2",
                         "Table", "101", "y", "Wood", "m", "", "1", "3",
                         "Lamp", "50", "n", "y", "Sams Choice", "110", "",
                         "2", "3", "", "2", "4", "", "q"
                     ]
        with patch('builtins.input', side_effect=input_vars):
            with self.assertRaises(SystemExit):
                 main.main()
