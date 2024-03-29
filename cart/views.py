from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from products.models import Product


# Create your views here.
def view_cart(request):
    """ A view that shows the shopping cart contents page """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a product to the shopping cart """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f"{product.name} quantity updated to {cart[item_id]}.")
    else:
        cart[item_id] = quantity
        messages.success(request, f"{product.name} has been added to your cart.")

    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):
    """ Update the quantity of a product in the shopping cart """
    try:
        if request.method == 'POST':
            product = get_object_or_404(Product, pk=item_id)
            quantity = int(request.POST.get('quantity'))
            cart = request.session.get('cart', {})
            
            if quantity > 0 and quantity < 100:
                cart[item_id] = quantity
                messages.success(request, f"Quantity of {product.name} updated to {cart[item_id]}.")
            else:
                del cart[item_id]  # Remove the item if the quantity is 0 or invalid
                messages.success(request, f"Removed {product.name}.")

            request.session['cart'] = cart
            
        return HttpResponseRedirect(reverse('view_cart'))
    except Exception as e:
        messages.error(request, f"Error updating cart: {(e)}")
        return HttpResponse(status=500)
