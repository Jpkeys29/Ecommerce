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

            