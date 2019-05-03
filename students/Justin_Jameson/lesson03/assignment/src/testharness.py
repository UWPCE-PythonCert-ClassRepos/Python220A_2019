# -------------------------------------------------#
# # Title: Lesson 03 Test Harness
# # Dev:   Justin Jameson
# # Date:  4/20/2019
# # ChangeLog: (Who, when, What)
# -------------------------------------------------#
"""
    Run pytest

"""

import pytest

import basic_operations as the_one_to_test

@pytest.fixture
def _add_customer():
    return [
        {customer_id:"0U812", first_name:"Justin", last_name:"Slog", home_address:"Poulsbo", phone_number:"12345", email_address:"email", customer_status:"active", credit_limit: 999},
        {customer_id:"B4UG0", first_name:"Kilee", last_name:"Bounce", home_address:"poulsbo", phone_number:"987654", email_address:"email", customer_status:"inactive", credit_limit: 10},
        {customer_id:"1L2AF", first_name:"Dana", last_name:"Scar", home_address:"P-bo", phone_number:"567654", email_address:"email", customer_status: "active", credit_limit: 6969},
        {customer_id:"N1K3", first_name:"Ethon", last_name:"Beanie", home_address:"Same", phone_number:"765432345678", email_address:"email", customer_status:"active", credit_limit: 7},
        {customer_id:"3NUF7", first_name:"Juston", last_name:"Knat", home_address:"new", phone_number:"098765432", email_address:"email", customer_status:"active", credit_limit: -10},
        {customer_id:"3RDB0Y", first_name:"Jordon", last_name:"Sauce", home_address:"duplicate", phone_number:"10239487", email_address:"email", customer_status:"active", credit_limit: -421},
        {customer_id:"Y3113R", first_name:"Katee", last_name:"NOPE", home_address:"somewere", phone_number:"comeon", email_address:"email", customer_status:"active", credit_limit: 456}
    ]