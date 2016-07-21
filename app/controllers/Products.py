"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Products(Controller):
    def __init__(self, action):
        super(Products, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('Product')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):
        """
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_users()
        
        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask
        
        # return self.load_view('index.html', messages=messages, user=user)
        """
        product_table = self.models['Product'].get_all_products()
        return self.load_view('products.html', product_table = product_table)
    
    def create(self, method="POST"):
        product_details = {
            'name': request.form['name'],
            'description': request.form['description'],
            'price': request.form['price']
            }
        self.models['Product'].add_product(product_details)
        return redirect('/products')

    def new(self):
        return self.load_view('new.html')

    def show(self, product_id):
        product = self.models['Product'].get_product_by_id(product_id)
        return self.load_view('show.html', product=product)
    def update(self, product_id):
        # in actuality, data for updating the course would come 
        # from a form on our client
        product_details = {
            'name': request.form['name'],
            'description': request.form['description'],
            'price': request.form['price'],
            'id': product_id
        }
        print product_details
        self.models['Product'].update_product(product_details)
        return redirect('/products')
        
    def edit(self, product_id):
        product = self.models['Product'].get_product_by_id(product_id)
        session['id']=product[0]['id']
        return self.load_view('edit.html', product=product)
    def destroy(self, product_id):
         self.models['Product'].delete_product(product_id)
         return redirect('/products')
