
import sys
import logging
from src import customer_class
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_new_customer():
    new_customer = customer_class.CustomerInformationClass(
         first_name=input("Enter Customers first name: "),
         last_name=input("Enter Customers first name: "),
         home_address=input("Enter the Customers Home Address: "),
         phone_number=input("Enter the Customers Phone Number: "),
         email_address=input("Enter the Customers Email: "),
         customer_status=input("Enter the Customers Status (Active/Inactive):"),
         credit_limit=input("Enter the Customers Credit Limit "),
         customer_id=input("Enter Customer ID: "))
    logger.info('crate_new _customer parameters entered.')



if __name__ == "__main__":
    create_new_customer()

