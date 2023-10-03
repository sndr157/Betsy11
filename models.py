import os
from peewee import Model, CharField, IntegerField, ForeignKeyField, SqliteDatabase, TextField, DecimalField
from decimal import ROUND_DOWN

class DatabaseManager:
    def __init__(self, db):
        self.db = db
    def __enter__(self):
        self.db.connect()
    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self.db.is_closed():
            self.db.close()

# get the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_directory, 'betsy.db')

# Create database object with foreign keys turned on
db = SqliteDatabase(db_path, pragmas={'foreign_keys': 1})

# BaseModel to inherit database
class BaseModel(Model):
    class Meta:
        database = db

# User Model
class User(BaseModel):
    name = CharField(max_length=255)
    email = CharField(max_length=255, unique=True)
    card_number = CharField(max_length=20)

# Tag Model
class Tag(BaseModel):
    tag = CharField(max_length=50, unique=True)

# Product Model
class Product(BaseModel):
    seller = ForeignKeyField(User, backref='products', on_delete='CASCADE')
    name = CharField(max_length=50, unique=True)
    description = TextField()
    price = DecimalField(max_digits=10, decimal_places=2, rounding=ROUND_DOWN)  # Change to DecimalField
    quantity = IntegerField()
    tag = ForeignKeyField(Tag, backref='products', on_delete='CASCADE')

# Transaction Model
class Transaction(BaseModel):
    buyer = ForeignKeyField(User, backref='transactions', on_delete='CASCADE')
    product = ForeignKeyField(Product, backref='transactions', on_delete='CASCADE')
    quantity = IntegerField()
    
# Create tables
with DatabaseManager(db) as manager:
    db.create_tables([User, Tag, Product, Transaction])
