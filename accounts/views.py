from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import stripe
import json
import djstripe
from django.http import JsonResponse, HttpResponse
from djstripe.models import Product
from .forms import SignupForm, LoginForm

from django.conf import settings


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            user = form.save()

            authenticate(username=user.username, password=user.password)

            if user is not None:
                login(request, user)


                return redirect('/dashboard')

    
    else: 
        form = SignupForm()
    
    return render(request, 'accounts/signup.html', {
        'form': form
    })


@login_required

def checkout(request):
    products = Product.objects.all()
    return render(request, 'accounts/checkout.html', {
        'products': products,
    })


@login_required
def create_sub(request):
  if request.method == 'POST':
      # Reads application/json and returns a response
      data = json.loads(request.body)
      payment_method = data['payment_method']
    #   stripe.api_key = djstripe.settings.STRIPE_TEST_SECRET_KEY
      stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

      payment_method_obj = stripe.PaymentMethod.retrieve(payment_method)
      djstripe.models.PaymentMethod.sync_from_stripe_data(payment_method_obj)


      try:
          # This creates a new Customer and attaches the PaymentMethod in one API call.
          customer = stripe.Customer.create(
              payment_method=payment_method,
              email=request.user.email,
              invoice_settings={
                  'default_payment_method': payment_method
              }
          )

          djstripe_customer = djstripe.models.Customer.sync_from_stripe_data(customer)
          request.user.customer = djstripe_customer
         

          # At this point, associate the ID of the Customer object with your
          # own internal representation of a customer, if you have one.
          # print(customer)

          # Subscribe the user to the subscription created
          subscription = stripe.Subscription.create(
              customer=customer.id,
              items=[
                  {
                      "price": data["price_id"],
                  },
              ],
              expand=["latest_invoice.payment_intent"]
          )

          djstripe_subscription = djstripe.models.Subscription.sync_from_stripe_data(subscription)

          request.user.subscription = djstripe_subscription
          request.user.save()

          return JsonResponse(subscription)
      except Exception as e:
          return JsonResponse({'error': (e.args[0])}, status =403)
  else:
    return HttpResponse('request method not allowed')
  

def complete(request):
  return render(request, "accounts/complete.html")