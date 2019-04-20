# -------------------------------------------------#
# # Title: Main module for inventory Management
# # Dev:   unknown
# # Date:  4/16/2019
# # ChangeLog: (Who, What)
# Justin Jameson
# Added doc strings
# shortened lines to conform to PEP 8
# method 'add_new_item' removed global FULL_INVENTORY;
# added doc strings.
# #-------------------------------------------------#
""" Launches the user interface for the Inventory management system"""

import sys
import market_prices
import inventory_class
import furniture_class
import electric_appliances_class


def main_menu(user_prompt=None):
    """"This method is the menu for the program. The intent is to
    offer (3) choices, add an item, retrieve information from an existing
    item, and exit the program."""
    valid_prompts = {"1": add_new_item,
                     "2": item_info,
                     "q": exit_program}
    options = list(valid_prompts.keys())

    while user_prompt not in valid_prompts:
        options_str = ("{}" + ", {}" * (len(options)-1)).format(*options)
        # look at the format string with the use of f and options at the end.
        print(f"Please choose from the following options ({options_str}):")
        print("1. Add a new item to the Inventory")
        print("2. Get item information")
        print("q. Quit")
        user_prompt = input(">")
    return valid_prompts.get(user_prompt)


def get_price(item_code):
    """This method is incomplete, I suspect it will
    be incorporated in the future with code from below
    item_price = market_prices.get_latest_price(item_code)"""
    # print("Get price")
    item_price = market_prices.get_latest_price(item_code)


def add_new_item():
    """Adding items to inventory. This method will add user
    input into a dictionary"""
    item_code = input("Enter item code: ")
    item_description = input("Enter item description: ")
    item_rental_price = input("Enter item rental price: ")

    # Get price from the market prices module
    item_price = market_prices.get_latest_price(item_code)

    is_furniture = input("Is this item a piece of Furniture? (Y/N): ")
    if is_furniture.lower() == "y":
        item_material = input("Enter item material: ")
        item_size = input("Enter item size (S,M,L,XL): ")
        new_item = furniture_class.Furniture(item_code,
                                             item_description,
                                             item_price,
                                             item_rental_price,
                                             item_material,
                                             item_size)
    else:
        is_electric_appliance = input("Is this item an electric appliance?"
                                      " (Y/N): ")
        if is_electric_appliance.lower() == "y":
            item_brand = input("Enter item brand: ")
            item_voltage = input("Enter item voltage: ")
            new_item = \
                electric_appliances_class.ElectricAppliances(item_code,
                                                             item_description,
                                                             item_price,
                                                             item_rental_price,
                                                             item_brand,
                                                             item_voltage)
        else:
            new_item = inventory_class.Inventory(item_code,
                                                 item_description,
                                                 item_price,
                                                 item_rental_price)
    FULL_INVENTORY[item_code] = new_item.return_as_dictionary()
    print("New Inventory item added")


def item_info():
    """ This method prints the dictionary"""
    item_code = input("Enter item code: ")
    if item_code in FULL_INVENTORY:
        print_dict = FULL_INVENTORY[item_code]
        for k, value in print_dict.items():
            print("{}:{}".format(k, value))
    else:
        print("Item not found in Inventory")


def exit_program():
    """This method exits the program"""
    sys.exit()


if __name__ == '__main__':
    FULL_INVENTORY = {}
    while True:
        print(FULL_INVENTORY)
        main_menu()()
        input("Press Enter to continue...........")
