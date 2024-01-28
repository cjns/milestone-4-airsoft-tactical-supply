from django.http import HttpResponse


class StripeWH_Handler:
    """
    Class to handle Stripe webhooks. Each method in this class corresponds to a different type of webhook event.
    """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Default method to handle any unhandled or unexpected webhook events. Returns a HTTP response with a message indicating the event type.
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the 'payment_intent.succeeded' webhook from Stripe. This event is sent when a payment intent has been successfully completed. Returns a HTTP response with a message indicating the event type.
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the 'payment_intent.payment_failed' webhook from Stripe. This event is sent when a payment intent has failed. Returns a HTTP response with a message indicating the event type.
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
    