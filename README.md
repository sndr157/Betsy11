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
