from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import stripe
from django.conf import settings
from .webhook_handler import StripeWH_Handler 

@csrf_exempt
@require_POST
def webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WH_SECRET
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(status=400)

    handler = StripeWH_Handler(request)
    try:
        response = handler.handle_event(event)
        return response
    except Exception as e:
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | ERROR: {e}',
            status=500)