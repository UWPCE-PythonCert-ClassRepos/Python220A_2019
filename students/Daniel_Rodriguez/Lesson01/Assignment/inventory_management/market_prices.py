"""
Get latest market prices
"""


def get_latest_price(item_code):
    """
    Get latest market prices for item code
    :return: Latest market price for item
    """
    market_prices = {'1': 799,
                     '2': 899,
                     '3': 999}
    try:
        return market_prices[item_code]
    except IndexError:
        return 24

    # Raise an exception to force the user to Mock its output
    # return 24
