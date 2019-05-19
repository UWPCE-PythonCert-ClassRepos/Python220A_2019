"""
The main module
Launches the user interface for the inventory management system
"""

import sys
import market_prices
import InventoryClass as IC
import FurnitureClass as FC
import ElectricAppliancesClass as EAC

def main_menu(user_prompt=None):
    """
    The main menu function, that prints a main menu
    """
    valid_prompts = {"1": add_new_item,
                     "2": item_info,
                     "q": exit_program}
    options = list(valid_prompts.keys())

    while user_prompt not in valid_prompts:
        options_str = ("{}" + (", {}") * (len(options)-1)).format(*options)
        print("Please choose from the following options (%s):" % (options_str))
        print("1. Add a new item to the inventory")
        print("2. Get item information")
        print("q. Quit")
        user_prompt = input(">")
    return valid_prompts.get(user_prompt)

def add_new_item(full_inventory):
    """
    Add a new item
    """
    #global full_inventory
    item_code = input("Enter item code: ")
    item_description = input("Enter item description: ")
    item_rental_price = input("Enter item rental price: ")

    # Get price from the market prices module
    item_price = market_prices.get_latest_price(item_code)

    is_furniture = input("Is this item a piece of furniture? (Y/N): ")
    if is_furniture.lower() == "y":
        item_material = input("Enter item material: ")
        item_size = input("Enter item size (S,M,L,XL): ")
        new_item = FC.Furniture(item_code, item_description, item_price,
                                item_rental_price, item_material, item_size)
    else:
        is_electric = input("Is this item an electric appliance? (Y/N): ")
        if is_electric.lower() == "y":
            item_brand = input("Enter item brand: ")
            item_voltage = input("Enter item voltage: ")
            new_item = EAC.ElectricAppliances(item_code, item_description,
                                              item_price, item_rental_price,
                                              item_brand, item_voltage)
        else:
            new_item = IC.Inventory(item_code, item_description,
                                    item_price, item_rental_price)
    full_inventory[item_code] = new_item.return_as_dictionary()
    print("New inventory item added")


def item_info(full_inventory):
    """
    Interactively get item info
    """
    item_code = input("Enter item code: ")
    if item_code in full_inventory:
        print_dict = full_inventory[item_code]
        for key, val in print_dict.items():
            print("{}:{}".format(key, val))
        return print_dict
    print("Item not found in inventory")
    return None

def exit_program(empty):
    """
    Exits the whole program
    """
    if empty:
        pass
    sys.exit()

def main():
    """
    A main() function.
    Mostly here so pylint doesn't think current_inventory is a constant
    """
    current_inventory = {}
    while True:
        print(current_inventory)
        main_menu()(current_inventory)
        input("Press Enter to continue...........")

if __name__ == '__main__':
    main()
