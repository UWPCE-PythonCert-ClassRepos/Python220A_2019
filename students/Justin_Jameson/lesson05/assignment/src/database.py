directory_name = '..\\.\\data\\'
product_data = 'product.csv'
customer_data = 'customers.csv'
rentals_data = 'rental.csv'
data_files = product_data, customer_data, rentals_data,

"""
    As a HP Norton customer I want to see a list of all products available for rent so that I can make a rental choice.
    You can have a specific field to indicate if a product is available, however,
    a quantity_available of 0 is understood as “not available”.

    As a HP Norton salesperson I want to see:
     1. a list of all of the different products, showing product ID, description, product type and quantity available.
     2. a list of the names and contact details (address, phone number and email) of all customers who have rented
        a certain product.

Here is what you need to do:

    1. Create a product database with attributes that reflect the contents of the csv file.
    2. Import all data in the csv files into your MongoDB implementation.
    3. Write queries to retrieve the product data.
    4. Write a query to integrate customer and product data (join data).

Other requirements:

    Your code should not trigger any warnings or errors from Pylint.

Testing

In order for your code to be evaluated, you need to create a file called database.py with the following functions:

    def import_data(directory_name, product_file, customer_file, rentals_file):
        This function takes a directory name and three csv files as input,then creates and populates a new MongoDB
        database.
           1. product data = product.csv
           2. customer data = customers.csv
           3. rentals data = rental.csv
        Return: 2 tuples:
        1. a record count of the number of products, customers and rentals added (in that order)
        2. a count of any errors that occurred, in the same order."""
def import_data(directory_name, product_file, customer_file, rental_file):

    """
    def show_available_products():
        Returns a Python dictionary of products listed as available with the following fields:
            product_id.
            description.
            product_type.
            quantity_available.

         For example:

         {‘prd001’:{‘description’:‘60-inch TV stand’,’product_type’:’livingroom’,’quantity_available’:‘3’},’prd002’:
         {‘description’:’L-shaped sofa’,’product_type’:’livingroom’,’quantity_available’:‘1’}}

    def show_rentals(product_id):
        Returns a Python dictionary with the following user information from users that have rented products matching product_id:
            user_id.
            name.
            address.
            phone_number.
            email.

         For example:

         {‘user001’:{‘name’:’Elisa Miles’,’address’:‘4490 Union Street’,’phone_number’:‘206-922-0882’,’email’:’elisa.miles@yahoo.com’},
         ’user002’:{‘name’:’Maya Data’,’address’:‘4936 Elliot Avenue’,’phone_number’:‘206-777-1927’,’email’:’mdata@uw.edu’}}

"""
