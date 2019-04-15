import sys
sys.path.append("inventory_management")

from unittest import TestCase
from unittest.mock import MagicMock, patch

from inventory_management.InventoryClass import Inventory
from inventory_management.ElectricAppliancesClass import ElectricAppliances
from inventory_management.FurnitureClass import Furniture
from inventory_management import main
from inventory_management import market_prices

class FurnitureTests(TestCase):
    """
    Tests for the Furniture class
    """
    def setUp(self):
        """
        Sets up tests for Furniture
        """
        self.item = Furniture('11', 'sofa', '4', '5', 'suede', 'xl')

    def test_init(self):
        """
        Test ElectricAppliances.__init__()
        """
        self.assertEqual(self.item.material, 'suede')
        self.assertEqual(self.item.size, 'xl')
        self.assertEqual(self.item.description, 'sofa')

    def test_dict(self):
        """
        Test Furniture.return_as_dictionary()
        """
        self.assertEqual(self.item.return_as_dictionary(),
                         {
                             'product_code': '11',
                             'description': 'sofa',
                             'market_price': '4',
                             'rental_price': '5',
                             'material': 'suede',
                             'size': 'xl'
                         })

class ElectricAppliancesTests(TestCase):
    """
    Tests for the ElectricAppliances class
    """
    def setUp(self):
        """
        Sets up tests for ElectricAppliances
        """
        self.item = ElectricAppliances('10', 'test', '4', '5', 'GE', '110')

    def test_init(self):
        """
        Test ElectricAppliances.__init__()
        """
        self.assertEqual(self.item.voltage, '110')
        self.assertEqual(self.item.brand, 'GE')
        self.assertEqual(self.item.description, 'test')

    def test_dict(self):
        """
        Test ElectricAppliances.return_as_dictionary()
        """
        self.assertEqual(self.item.return_as_dictionary(),
                         {
                             'product_code': '10',
                             'description': 'test',
                             'market_price': '4',
                             'rental_price': '5',
                             'brand': 'GE',
                             'voltage': '110'
                         })

class MarketPricesTests(TestCase):
    """
    Tests for market_prices.py
    """
    def test_get_latest_price(self):
        """
        Tests get_latest_price()
        """
        self.assertEqual(market_prices.get_latest_price('10'), 24)

class MainTests(TestCase):
    """
    Tests for main.py
    """
    def test_main_menu(self):
        """
        Tests main.main_menu()
        """
        self.assertEqual(main.main_menu('1'), main.add_new_item)
        self.assertEqual(main.main_menu('2'), main.item_info)
        self.assertEqual(main.main_menu('q'), main.exit_program)
        with patch('builtins.input', lambda x: '1'):
            menu = main.main_menu()
            self.assertEqual(menu, main.add_new_item)
    
    def test_add_new_item(self):
        """
        Tests main.add_new_item()
        """
        input_vars = ['3', 'Car', '1', 'n', 'n']
        inventory = {}
        with patch('builtins.input', side_effect=input_vars):
            main.add_new_item(inventory)
        self.assertEqual(inventory['3'],
                         {
                             'product_code': '3',
                             'description': 'Car',
                             'market_price': 24,
                             'rental_price': '1'
                         })

    def test_add_new_furniture(self):
        """
        Tests main.add_new_item() with a furniture item
        """
        input_vars = ['4', 'Rug', '1', 'y', 'Berber', 's']
        inventory = {}
        with patch('builtins.input', side_effect=input_vars):
            main.add_new_item(inventory)
        self.assertEqual(inventory['4'],
                         {
                             'product_code': '4',
                             'description': 'Rug',
                             'market_price': 24,
                             'rental_price': '1',
                             'material': 'Berber',
                             'size': 's'
                         })

    def test_add_new_electric(self):
        """
        Tests main.add_new_item() with an electric appliance
        """
        input_vars = ['5', 'Shaver', '1', 'n', 'y', 'Norelco', '110']
        inventory = {}
        with patch('builtins.input', side_effect=input_vars):
            main.add_new_item(inventory)
        self.assertEqual(inventory['5'],
                         {
                             'product_code': '5',
                             'description': 'Shaver',
                             'market_price': 24,
                             'rental_price': '1',
                             'brand': 'Norelco',
                             'voltage': '110'
                         })

    def test_item_info(self):
        """
        Tests main.item_info()
        """
        input_vars = ['6', '99']
        test_item = {'product_code': '6',
                     'description': 'item',
                     'market_price': 24,
                     'rental_price': '1'}
        inventory = {'6': test_item}
        with patch('builtins.input', side_effect=input_vars):
            item = main.item_info(inventory)
            bogus_item = main.item_info(inventory)
        self.assertEqual(item, test_item)
        self.assertEqual(bogus_item, None)

    def test_exit(self):
        """
        Tests main.exit_program()
        """
        with self.assertRaises(SystemExit):
            main.exit_program(None)
            main.exit_program("exit")

    def test_main_main(self):
        """
        Tests main.main()
        """
        input_vars = ['q']
        with patch('builtins.input', side_effect=input_vars):
            with self.assertRaises(SystemExit):
                main.main()
        
