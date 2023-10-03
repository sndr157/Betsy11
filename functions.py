from rich.table import Table
from rich.console import Console

# Importing the models created in models.py file
from models import (
	User,
	Tag,
	Product,
	Transaction,
)

# BASIC UTILITIES NEEDED
class Utils:
	def clean_str(self, str):
		return str.lower().strip()
	
	def remove_invalid(self, str):
		alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
		new_str = ""
		for i in str:
			if i in alpha:
				new_str += i
		return new_str
	
	def display_table(self, data, title="", mapper={}):
		if len(data) == 0:
			print(f"NO DATA TO SHOW FOR: {title}", end=' ---> ')
			return

		columns = data[0].__class__._meta.fields

		# creating table
		table = Table(title=title, show_header=True, header_style="bold magenta")

		# adding header
		[table.add_column(col) for col in columns]

		# adding rows
		for record in data:
			row = []
			for k in columns.keys():
				v = getattr(record, k)
				if k in mapper:
					_v = mapper[k](v)
					v = f"{_v} ({v})"
				v = str(v)
				row.append(v)
			table.add_row(*row)

		# displaying the table
		console = Console()
		console.print(table)

# SEARCHING ALGORITHMS
class SearchAlgorithms(Utils):
	def advanced_search(self, str1, str2):
		# uses name + description
		# used in product search by term
		str1 = self.clean_str(str1)
		str1 = self.remove_invalid(str1)
		str2 = self.clean_str(str2)
		str2 = self.remove_invalid(str2)

		return str1 in str2 or str2 in str1

	def simple_search(self, str1, str2):
		# uses name only
		str1 = self.clean_str(str1)
		str2 = self.clean_str(str2)
		return str1 in str2 or str2 in str1

# DISPLAYING CONTENT OF TABLES IN OUTPUT
class ShowTables(Utils):
	def show_users(self):
		records = list(User.select())
		self.display_table(
			records,
			title=f"Table: User",
			mapper={

			}
		)

	def show_tags(self):
		records = list(Tag.select())
		self.display_table(
			records,
			title=f"Table: Tag",
			mapper={

			}
		)

	def show_products(self):
		records = list(Product.select())
		self.display_table(
			records,
			title=f"Table: Product",
			mapper={
				"seller": lambda x: x.name,
				"tag": lambda x: x.tag
			},
		)

	def show_transactions(self):
		records = list(Transaction.select())
		self.display_table(
			records,
			title=f"Table: Transaction",
			mapper={
				"buyer": lambda x: x.name,
				"product": lambda x: x.name,
			}
		)

# QUERYING METHODS ARE IMPLEMENTED HERE
class Operations(SearchAlgorithms, ShowTables):
	def __init__(self, db_manager):
		self.db = db_manager

	def search_product_by_term(self, name):
		matches = []
		for product in Product.select():
			if self.advanced_search(product.name + product.description, name):
				matches.append(product)
		self.display_table(
			matches,
			title=f"Matches Found for: {name}",
			mapper={
				"seller": lambda x: x.name,
				"tag": lambda x: x.tag
			},
		)

	def search_product_by_user(self, name):
		matches = []
		for product in Product.select():
			if self.simple_search(product.seller.name, name):
				matches.append(product)
		self.display_table(
			matches,
			title=f"Products Sold By: {name}",
			mapper={
				"seller": lambda x: x.name,
				"tag": lambda x: x.tag
			},
		)

	def search_product_by_tag(self, name):
		matches = []
		for product in Product.select():
			if self.simple_search(product.tag.tag, name):
				matches.append(product)
		self.display_table(
			matches,
			title=f"Products with Tag: {name}",
			mapper={
				"seller": lambda x: x.name,
				"tag": lambda x: x.tag
			},
		)

	def add_product_user(self, product_id, user_id):
		product = Product.get_by_id(product_id)
		user = User.get_by_id(user_id)
		product.seller = user
		product.save()

	def remove_product_user(self, product_id):
		product = Product.get_by_id(product_id)
		user = User.get_by_id(1)
		product.seller = user
		product.save()

	def update_quantity(self, product_id, new_quantity):
		product = Product.get_by_id(product_id)
		product.quantity = new_quantity
		product.save()

	def purchase(self, user_id, product_id, quantity):
		user = User.get_by_id(user_id)
		product = Product.get_by_id(product_id)

		if product.quantity < quantity:
			return

		# updating quantity in product
		product.quantity -= quantity
		product.save()

		# updating transaction table
		Transaction(
			buyer=user,
			product=product,
			quantity=quantity  # Replace with the actual quantity
		).save()
