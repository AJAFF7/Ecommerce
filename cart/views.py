from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib import messages
#import logging
# Create your views here.
def cart_summary(request):
    # Get the cart
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    return render(request, 'cart_summary.html', {"cart_products": cart_products, "quantities": quantities})

def cart_add(request):
    # Get the cart
    cart = Cart(request)

    # Test for Post
    if request.POST.get('action') == 'post':
        # Get Stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        # Look for Product In DB
        product = get_object_or_404(Product, id=product_id)
        # Save To Session
        cart.add(product=product, quantity=product_qty)

        # Get Cart Quantity
        cart_quantity = cart.__len__()
        # Return Reponse
        response = JsonResponse({'qty': cart_quantity})
#        messages.success(request, ("product added to Card..."))
        return response




def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # Get Stuff
        product_id = int(request.POST.get('product_id'))
        # Call delete Function in Cart
        cart.delete(product=product_id)

        response = JsonResponse({'product': product_id})
        return response

def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # Get Stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        cart.update(product_id=product_id, quantity=product_qty)

        response = JsonResponse({'qty': product_qty})
        return response
        # return redirect('cart_summary')










