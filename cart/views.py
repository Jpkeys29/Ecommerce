from django.shortcuts import render
from .cart import Cart
from store.models import Product
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

def cart_summary(request):
    cart = Cart(request)
    return render(request, 'cart/cart-summary.html', {'cart':cart})

def cart_add(request):
    cart = Cart(request)

    # To check if we are getting an AJAX request:
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))
        #Getting a object from the model 'product' with id from product id from ajax request
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, product_qty = product_quantity)
        # To return session data after several products to the cart:
        cart_quantity = cart.__len__()
        response = JsonResponse({'qty': cart_quantity})
        return response

def cart_update(request):
    pass

def cart_delete(request):
    pass

