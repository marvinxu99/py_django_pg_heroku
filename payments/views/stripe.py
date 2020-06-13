from django.conf import settings
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
import stripe


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        # domain_url = 'http://localhost:8000/payments/'
        successful_url = request.build_absolute_uri(reverse('payments:success'))
        cancelled_url = request.build_absolute_uri(reverse('payments:cancelled'))

        stripe.api_key = settings.STRIPE_SECRET_KEY
        
        try:
            # Create new Checkout Session for the order
            # Other optional params include:
            # [billing_address_collection] - to display billing address details on the page
            # [customer] - if you have an existing Stripe Customer ID
            # [payment_intent_data] - lets capture the payment later
            # [customer_email] - lets you prefill the email input in the form
            # For full details see https:#stripe.com/docs/api/checkout/sessions/create

            # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
            checkout_session = stripe.checkout.Session.create(
                # success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                # cancel_url=domain_url + 'cancelled/',
                success_url=successful_url + '?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=cancelled_url,
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'name': 'Winn Issue Tracker Software',
                        'quantity': 1,
                        'currency': 'usd',
                        'amount': '20000',
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})

