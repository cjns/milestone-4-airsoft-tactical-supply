from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def view_cart(request):
    """ A view that shows the shopping cart contents page """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a product to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):
    """ Update the quantity of a product in the shopping cart """
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        cart = request.session.get('cart', {})
        
        if quantity > 0 and quantity < 100:
            cart[item_id] = quantity
        else:
            del cart[item_id]  # Remove the item if the quantity is 0 or invalid

        request.session['cart'] = cart
        
    return HttpResponseRedirect(reverse('view_cart'))
