import csv
list_of_customers = []
list_of_products = []
list_of_rentals = []
with open('customers.csv', 'r') as customer:
    reader = csv.reader(customer)
    for row in reader:
        c_dict = {'User ID': row[0], 'Name': row[1], 'Address': row[2],
                  'zip code': row[3], 'phone number': row[4], 'email': row[5]}
        list_of_customers.append(c_dict)
    list_of_customers.pop(0)
with open('product.csv', 'r') as product:
    reader = csv.reader(product)
    for row in reader:
        p_dict = {'Product ID': row[0], 'Description': row[1], 'Product Type': row[2], 'Quantity available': row[3]}
        list_of_products.append(p_dict)
    list_of_products.pop(0)
with open('rental.csv', 'r') as rentals:
    reader = csv.reader(rentals)
    for row in reader:
        r_dict = {'Product ID': row[0], 'User ID': row[1]}
        list_of_rentals.append(r_dict)
    list_of_rentals.pop(0)
print(list_of_customers)
print(list_of_products)
print(list_of_rentals)
