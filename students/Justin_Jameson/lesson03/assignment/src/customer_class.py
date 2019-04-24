# -------------------------------------------------#
# # Title: Lesson 03 customer_class
# # Dev:   Justin Jameson
# # Date:  4/20/2019
# # ChangeLog: (Who, when, What)
# -------------------------------------------------#

""" Establishing a class to collect Customer Information"""


class CustomerInformationClass:
    """
    This class creates attributes for collecting Customer information. The attributes will be
    used for database integration.
    """

    def __init__(self, customer_id, first_name, last_name, home_address, phone_number,
                 email_address, customer_status, credit_limit):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.home_address = home_address
        self.phone_number = phone_number
        self.email_address = email_address
        self.customer_status = customer_status
        self.credit_limit = credit_limit


    def return_as_dictionary(self):
        """
        Returns Class Representation as a Dictionary
        :return: Dictionary Representation of the customer information
        class
        """
        customer_dict = {}
        customer_dict['customer_id'] = self.customer_id
        customer_dict['first_name'] = self.first_name
        customer_dict['last_name'] = self.last_name
        customer_dict['home_address'] = self.home_address
        customer_dict['phone_number'] = self.phone_number
        customer_dict['email_address'] = self.email_address
        customer_dict['customer_status'] = self.customer_status
        customer_dict['credit_limit'] = self.credit_limit

        return customer_dict

    def return_as_list(self):
        """
        Returns Class Representation as a list
        :return: list Representation of the customer information
        class
        """
        customer_list = [(self.customer_id,
                         self.first_name,
                         self.last_name,
                         self.home_address,
                         self.phone_number,
                         self.email_address,
                         self.customer_status,
                         self.credit_limit), ]

        return customer_list

