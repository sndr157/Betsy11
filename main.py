from models import db, DatabaseManager
from functions import Operations

if __name__ == '__main__':
	with DatabaseManager(db) as db_manager:

		# Creating Instance for query operations
		ops = Operations(db_manager)

		# Showing current data
		ops.show_products()
		ops.show_tags()
		ops.show_transactions()
		ops.show_users()

		# QUERY OPERATIONS

		# lists products having this name
		ops.search_product_by_term(name="phone")
		# lists products sold by users having this name
		ops.search_product_by_user(name="ja")
		# lists product with this tag
		ops.search_product_by_tag(name="electronics")
		# removes seller from a product
		ops.remove_product_user(product_id=5)
		# attaches a seller to a user
		ops.add_product_user(
			product_id=5,
			user_id=3,
		)
		# updates the quantity
		ops.update_quantity(
			product_id=2,
			new_quantity=5,
		)
		# this undergoes a transaction
		ops.purchase(
			user_id=8,
			product_id=1,
			quantity=2,
		)

		# Showing data after query operations
		ops.show_products()
		ops.show_tags()
		ops.show_transactions()
		ops.show_users()
