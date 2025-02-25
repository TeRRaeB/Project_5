from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
        bag = request.session.get('bag',{})
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment.")
            return redirect(reverse('products'))
        order_form = OrderForm()
        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': 'pk_test_51QwLg2RhkQw6p57bvpuKHUWIzuVVvvNUzX3t2o0QmvyBI7FrsnkHkNSYjnUkPoePwO7qRBHTdjXutQq4lWAHHnuR00tTB84q6Z',
            'stripe_secret': 'sk_test_51QwLg2RhkQw6p57bzp83Xk9Djy5BrI8R3EAE29xi2kosm2E0ayfH1mqHaB4d5K6uG0FCzpEkJmQ7LIdNlT6wWy2W00GzAh8EsK',
            }
        
        return render(request,template,context)