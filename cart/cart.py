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

            