"""
This module is supposed to return the latest market price
"""

def get_latest_price(item_code):
    """
    This function returns 24.  All the time.  No matter what you input.
    Apparently this forces you to mock the output.
    """
    if item_code:
        pass
    return 24
    # Raise an exception to force the user to Mock its output (??)
