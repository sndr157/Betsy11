# Betsy11: A Homemade Goods Marketplace 🛍️🏡

## Description 📜

Welcome to Betsy11, your one-stop web marketplace for buying and selling homemade goods! 🪴🎨 Whether you're a creator or a shopper, Betsy11 has you covered. We've used the magical Peewee Python Object-Relational Mapping (ORM) library to create a seamless experience with our trusty `betsy.db` SQLite database. 🐍✨

## Database Models 📊

- **User**: Meet our users! They've got names, emails, and secret passwords! 🔐👥
- **Address**: These belong to our users and include fancy stuff like countries, states, and zip codes. 🌍🏠
- **PaymentInfo**: Securely stores card details for all your shopping sprees! 💳💸
- **Tag**: Tags help us categorize our homemade treasures. 🏷️
- **Product**: The stars of the show! Products come with sellers, names, and descriptions. Plus, we've got prices (in cents), quantities, and cool tags! 🌟🛒
- **Transaction**: When a purchase happens, we record it here, complete with buyers, products, and quantities. 💼💰

## Database Setup ⚙️

Getting started is easy-peasy! Run `models.py` to set up the database and tables. Just do this:

```python
import models
```

That's it! The database is ready to roll! 🎲🎉

## Issues and Solutions 


** Unhandled Database Connection Exception**
*Problem*: The code in Code Block 2 doesn't handle exceptions that may occur when establishing a database connection.
*Resolution*: Add exception handling to ensure graceful handling of database connection issues.

```python
# Code Block 2: Database Connection with Exception Handling
try:
    with DatabaseManager(db) as manager:
        # Perform database operations here
except Exception as e:
    print(f"Error: {e}")
```

** Incorrect Display of Table Headers**
*Problem*: The code in the `display_table` method of the `Utils` class does not display table headers correctly.
*Resolution*: Modify the `display_table` method to ensure that table headers are displayed properly.

```python
# Code Block 1: Modify display_table method
def display_table(self, data, title="", mapper={}):
    if len(data) == 0:
        print(f"NO DATA TO SHOW FOR: {title}", end=' ---> ')
        return

    columns = data[0].__class__._meta.fields

    # Creating table
    table = Table(title=title, show_header=True, header_style="bold magenta")

    # Adding header
    [table.add_column(col, header=col) for col in columns]  # Add header parameter

    # Rest of the method remains the same
    # ...
```

** Inefficient Product Search Algorithm**
*Problem*: The `search_product_by_term` method in the `Operations` class uses an inefficient algorithm for searching products by term.
*Resolution*: Optimize the search algorithm for better performance.

```python
# Code Block 1: Modify search_product_by_term method
class Operations(SearchAlgorithms, ShowTables):
    # ...

    def search_product_by_term(self, name):
        matches = []
        clean_name = self.clean_str(name)
        for product in Product.select().where(
                (fn.Lower(Product.name).contains(clean_name)) | (fn.Lower(Product.description).contains(clean_name))):
            matches.append(product)
        self.display_table(
            matches,
            title=f"Matches Found for: {name}",
            mapper={
                "seller": lambda x: x.name,
                "tag": lambda x: x.tag
            },
        )
```


## Interacting with the Database 💬

Once your database is set up and loaded with data, you're in business! Check out `main.py` to explore all the nifty functions:

- 🧐 **Search for Products**: Find hidden gems with search by terms!
- 🛒 **List User Products**: See what your favorite sellers are offering.
- 🏷️ **List Tag Products**: Dive into specific categories.
- 🛍️ **Add or Update Products**: Sellers, make your mark!
- 📦 **Update Stock**: Keep those shelves filled.
- ❌ **Remove Products**: When it's time to say goodbye.
- 💳 **Make Purchases**: Shop 'til you drop with automated stock updates!

## Testing 🧪

To put Betsy11 to the test, follow these steps:

1. Run `populate_test_data.py` to create and fill the database with data:

   ```bash
   python populate_test_data.py
   ```

2. Now, let's get to the fun part! Run `main.py` to experience all the database queries:

   ```bash
   python main.py
   ```

And there you have it—Betsy11 in action! 🚀

## Collaboration 🤝

Betsy11 is just getting started, and there's a whole world of enhancements and functionalities waiting to be added. Future plans include form validations, rock-solid user authorization, and even more complex search criteria. Interested in joining the party? Fork the repository and submit a pull request! 🎉🙌

## Disclaimer 🚨

While we're doing our best to make Betsy11 awesome, remember that it's still in its early stages. Bugs and issues might pop up unexpectedly. So, always keep your data and schemas backed up! 📂💼

## License 📝

Betsy11 is a project brought to you by Sandra Calzada. Enjoy shopping and creating with us! 🛒🌟🛍️
