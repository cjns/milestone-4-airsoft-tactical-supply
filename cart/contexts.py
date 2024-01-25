from decimal import Decimal
from django.conf import settings


def cart_contents(request):
    cart_items = []
    total_cost = 0
    total_products = 0
    delivery = 0
    free_delivery_delta = 0

    if total_cost < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total_cost * \
            Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total_cost

    total_cost_with_delivery = delivery + total_cost

    context = {
        'cart_items': cart_items,
        'total_cost': total_cost,
        'total_products': total_products,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'total_cost_with_delivery': total_cost_with_delivery,
    }

    return context
