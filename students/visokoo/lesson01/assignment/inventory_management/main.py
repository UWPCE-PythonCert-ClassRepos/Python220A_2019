"""
The purpose of this module is to launch the user interface for
the inventory management system
"""
import sys
from inventory_management import market_prices
from inventory_management import InventoryClass
from inventory_management import FurnitureClass
from inventory_management import ElectricAppliancesClass


def main_menu(user_prompt=None):
    """ Receive user input and use case dict to trigger function """
    valid_prompts = {"1": add_new_item,
                     "2": item_info,
                     "q": exit_program}
    options = list(valid_prompts.keys())

    while user_prompt not in valid_prompts:
        options_str = ("{}" + (", {}") * (len(options)-1)).format(*options)
        print(f"Please choose from the following options ({options_str}):")
        print("1. Add a new item to the inventory")
        print("2. Get item information")
        print("q. Quit")
        user_prompt = input(">")
    return valid_prompts.get(user_prompt)


def get_price(item_code):
    """ Grab price for respectice item code provided """
    price = FULL_INVENTORY[item_code]['rental_price']
    print(f"Price for item code: {item_code} is {price}")
    return price


def add_new_item():
    """ Add new inventory item """
    item_code = input("Enter item code: ")
    item_description = input("Enter item description: ")
    item_rental_price = input("Enter item rental price: ")

    # Get price from the market prices module
    item_price = market_prices.get_latest_price(item_code)

    is_furniture = input("Is this item a piece of furniture? (Y/N): ")
    if is_furniture.lower() == "y":
        item_material = input("Enter item material: ")
        item_size = input("Enter item size (S,M,L,XL): ")
        new_item = FurnitureClass.Furniture(
            item_code,
            item_description,
            item_price,
            item_rental_price,
            material=item_material,
            size=item_size)
    else:
        is_electric_appliance = input(
            "Is this item an electric appliance? (Y/N): ")
        if is_electric_appliance.lower() == "y":
            item_brand = input("Enter item brand: ")
            item_voltage = input("Enter item voltage: ")
            new_item = ElectricAppliancesClass.ElectricAppliances(
                item_code,
                item_description,
                item_price,
                item_rental_price,
                brand=item_brand,
                voltage=item_voltage)
        else:
            new_item = InventoryClass.Inventory(
                item_code,
                item_description,
                item_price,
                item_rental_price)
    FULL_INVENTORY[item_code] = new_item.return_as_dictionary()
    print("New inventory item added")
    return FULL_INVENTORY[item_code]


def item_info():
    """ Return item info if exists """
    item_code = input("Enter item code: ")
    if item_code in FULL_INVENTORY:
        print_dict = FULL_INVENTORY[item_code]
        output = []
        for key, value in print_dict.items():
            print(f"{key}: {value}")
            output.append(print_dict)
    else:
        output = "Item not found in inventory"
        print(output)
    return output


def exit_program():
    """ Exit the program """
    sys.exit()


FULL_INVENTORY = {}

if __name__ == '__main__':
    # FULL_INVENTORY = {}
    while True:
        for index, item in FULL_INVENTORY.items():
            print(f"{index}: {item}")
        main_menu()()
        input("Press Enter to continue...........")
