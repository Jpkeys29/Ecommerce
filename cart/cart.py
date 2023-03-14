from decimal import Decimal
from store.models import Product

class Cart():
    def __init__(self,request):

        #Creating a session:
        self.session = request.session

        #Returning customer - obtain their existing session. 'session_key' could be any other name
        cart = self.session.get('session_key')

        #New user - create a new session
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        #To have access to our cart from any page:
        self.cart = cart

    # It comes from the function cart.add from views
    def add(self,product,product_qty):
        product_id = str(product.id)

        # performing a test. If product is in the cart:
        if product_id in self.cart:
            self.cart[product_id]['qty'] = product_qty  #modifies the quantity of product
        else: #if the product does not exits in the user's car
            self.cart[product_id] = {'price': str(product.price), 'qty': product_qty} #then take the price along with quantity

        self.session.modified = True #Just telling Django that the session has been modified

    #To obtain the totals of products in session:
    def __len__(self):
        return sum(item['qty'] for item in self.cart.values())  

    # To loop(iter:iterate) through all the session data:
    def __iter__(self):
        all_product_ids = self.cart.keys()
        #to match all the products in the cart:
        products = Product.objects.filter(id__in=all_product_ids)
        #To copy an instance of session data:
        cart = self.cart.copy()
        #To loop through each product and add data from the database:
        for product in products:
            cart[str(product.id)]['product'] = product
            
        #To define price:
        for item in cart.values():
        #To import price from a string to decimals:
            item['price'] = Decimal(item['price'])
        #To create a total integer:
            item['total'] = item['price'] * item['qty']
        #To return the total price:
            yield item

    #To create a total price:
    def get_total(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())

    def delete(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified = True
           