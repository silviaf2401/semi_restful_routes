""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Product(Model):
    def __init__(self):
        super(Product, self).__init__()
    """
    Below is an example of a model method that queries the database for all users in a fictitious application
    
    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def get_user(self):
        query = "SELECT * from users where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

    def add_message(self):
        sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
        data = {'message': 'awesome bro', 'users_id': 1}
        self.db.query_db(sql, data)
        return True
    
    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    """
    def get_all_products(self):
        return self.db.query_db("SELECT id, name, description, price FROM products")

    def add_product(self, product_details):
      # Build the query first and then the data that goes in the query
        query = "INSERT INTO products (name, description, price) VALUES (:name, :description, :price)"
        data = {'name': product_details['name'], 'description': product_details['description'], 'price': product_details['price'] }
        return self.db.query_db(query, data)    

    def get_product_by_id(self, product_id):
        # pass data to the query like so
      query = "SELECT id, name, description, price FROM products WHERE id = :product_id"
      data = { 'product_id': product_id}
      return self.db.query_db(query, data)

    def update_product(self, product):
      # Building the query for the update
      query = "UPDATE products SET name=:name, description=:description, price=:price WHERE id = :product_id"
      # we need to pass the necessary data
      data = {'name': product['name'], 'description': product['description'], 'price': product['price'], 'product_id': product['id']}
      # run the update
      return self.db.query_db(query, data)      

    def delete_product(self, product_id):
      query = "DELETE FROM products WHERE id = :product_id"
      data = { "product_id": product_id}
      return self.db.query_db(query, data)  