# Import necessary modules and models from your original script
from peewee import SqliteDatabase
from models import User, Tag, Product, Transaction
from decimal import Decimal, ROUND_DOWN

# Define a function to populate data
def populate_data():
    # Open a connection to the database
    db = SqliteDatabase('betsy.db')

    # Sample data for users
    users_data = [
        # initial NULL User which mean no user
        {
            'name': 'None',
            'email': 'none@none.none',
            'card_number': '0000000000000000',
        },
        {
            'name': 'John Doe',
            'email': 'john@example.com',
            'card_number': '1234567890123456',
        },
        {
            'name': 'Jane Smith',
            'email': 'jane@example.com',
            'card_number': '9876543210987654',
        },
        {
            'name': 'James',
            'email': 'james@example.com',
            'card_number': '9876543298767654',
        },
        {
            'name': 'Charles',
            'email': 'charles@example.com',
            'card_number': '7654543210987654',
        },
        {
            'name': 'Henry',
            'email': 'henry@example.com',
            'card_number': '98765432198767654',
        },
        {
            'name': 'Joe Goldberg',
            'email': 'joe@example.com',
            'card_number': '98765432109876541',
        },
        {
            'name': 'Tokyo',
            'email': 'tokyo@example.com',
            'card_number': '98454545454987654',
        },
        # Add more user data as needed
    ]

    # Sample data for tags
    tags_data = [
        {'tag': 'Electronics'},
        {'tag': 'Clothing'},
        {'tag': 'Books'},
        # Add more tag data as needed
    ]

    # Sample data for products
    products_data = [
        {
            'seller': 2,  # Replace with the appropriate user ID
            'name': 'iPhone 14',
            'description': 'Get iPhone 14 and iPhone 14 Plus for an amazing price with special carrier trade-in offers',
            'price': Decimal('699.99').quantize(Decimal('0.01'), rounding=ROUND_DOWN),
            'quantity': 21,
            'tag': 1
        },
        {
            'seller': 3,  # Replace with the appropriate user ID
            'name': 'iPhone 13',
            'description': 'Apple iPhone 13 smartphone. Announced Sep 2021. Features 6.1″ display, Apple A15 Bionic chipset, 3240 mAh battery, 512 GB storage, 4 GB RAM',
            'price': Decimal('599.99').quantize(Decimal('0.01'), rounding=ROUND_DOWN),
            'quantity': 12,
            'tag': 1
        },
        {
            'seller': 4,  # Replace with the appropriate user ID
            'name': 'Gaming Laptop',
            'description': 'HP Victus 15 FA0044TX i7-12700H 16GB 512GB SSD Gaming Laptop.',
            'price': Decimal('1399.99').quantize(Decimal('0.01'), rounding=ROUND_DOWN),
            'quantity': 10,
            'tag': 1
        },
        {
            'seller': 5,  # Replace with the appropriate user ID
            'name': 'The Great Expectations',
            'description': 'Book by Charles Dickens',
            'price': Decimal('19.99').quantize(Decimal('0.01'), rounding=ROUND_DOWN),
            'quantity': 22,
            'tag': 2
        },
        {
            'seller': 6,  # Replace with the appropriate user ID
            'name': 'Old man and the sea',
            'description': 'Book by Ernest Hemingway',
            'price': Decimal('19.99').quantize(Decimal('0.01'), rounding=ROUND_DOWN),
            'quantity': 20,
            'tag': 2
        },
        {
            'seller': 7,  # Replace with the appropriate user ID
            'name': 'Black Nike Shoes',
            'description': 'Good for walk, run, stroll',
            'price': Decimal('299.99').quantize(Decimal('0.01'), rounding=ROUND_DOWN),
            'quantity': 5,
            'tag': 3
        },
        # Add more product data as needed
    ]

    # Sample data for transactions
    transactions_data = [
        {'buyer': 6, 'product': 1, 'quantity': 3},
        {'buyer': 7, 'product': 2, 'quantity': 1},
        {'buyer': 2, 'product': 3, 'quantity': 2},
        {'buyer': 3, 'product': 4, 'quantity': 1},
        {'buyer': 8, 'product': 5, 'quantity': 1},
        {'buyer': 5, 'product': 6, 'quantity': 1},
        {'buyer': 5, 'product': 6, 'quantity': 6},
        {'buyer': 5, 'product': 3, 'quantity': 1},
        {'buyer': 3, 'product': 2, 'quantity': 2},
        {'buyer': 2, 'product': 1, 'quantity': 3},
        # Add more transaction data as needed
    ]

    # Open a database transaction for bulk insertion
    with db.atomic():
        # Insert users
        User.insert_many(users_data).execute()

        # Insert tags
        Tag.insert_many(tags_data).execute()

        # Insert products
        Product.insert_many(products_data).execute()

        # Insert transactions
        Transaction.insert_many(transactions_data).execute()

if __name__ == "__main__":
    # Call the populate_data function to insert sample data into the database
    print("Populating the data .....", end=" ")
    populate_data()
    print("Done!")
