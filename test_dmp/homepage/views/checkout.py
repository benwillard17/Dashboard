from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django.shortcuts import redirect
from django_mako_plus.controller.router import get_renderer
from django.core.mail import send_mail
from django.contrib.auth.models import check_password
from django.contrib.auth import authenticate, login, logout
import random
import requests
from django.core.mail import EmailMultiAlternatives

API_URL = 'http://ithers.cs.byu.edu/iscore/api/v1/charges'
API_KEY = 'bd4c3e68deac00a9d76b8646e02eb328'

templater = get_renderer('homepage')


##########################################################################
# shows the list of products
@view_function
def process_request(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)

    params = {}

    try:
        user = hmod.User.objects.get(id=request.user.id)
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/accounts/')

    # create the form object
    # fill the form initially with data
    form = ShippingForm(initial={
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'address1': user.address1,
        'address2': user.address2,
        'city': user.city,
        'state': user.state,
        'zipcode': user.zipcode,
        'phone_number': user.phone_number,
    })
    if request.method == 'POST':
        form = ShippingForm(request.POST)
        form.userid = user.id
        if form.is_valid():
            return HttpResponse('<script> window.location.href = "/homepage/checkout.finalcheckout" </script>')

    # store the form in the parameters
    params['form'] = form
    params['user'] = user
    return templater.render_to_response(request, 'checkout.html', params)


class ShippingForm(forms.Form):
    first_name = forms.CharField(required=True, min_length=1, max_length=100, label="First Name", widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}))
    last_name = forms.CharField(required=True, min_length=1, max_length=100, label="Last Name", widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}))
    email = forms.EmailField(required=True, min_length=1, max_length=100, label="Email", widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    address1 = forms.CharField(required=True, min_length=1, max_length=100, label="Address", widget=forms.TextInput(attrs={'placeholder': 'Address', 'class': 'form-control'}))
    address2 = forms.CharField(required=False, min_length=1, max_length=100, label="Address 2", widget=forms.TextInput(attrs={'placeholder': 'Address 2', 'class': 'form-control'}))
    city = forms.CharField(required=True, min_length=1, max_length=100, label="City", widget=forms.TextInput(attrs={'placeholder': 'City', 'class': 'form-control'}))
    state = forms.CharField(required=True, min_length=1, max_length=100, label="State", widget=forms.TextInput(attrs={'placeholder': 'State', 'class': 'form-control'}))
    zipcode = forms.CharField(required=True, min_length=1, max_length=100, label="Zip", widget=forms.TextInput(attrs={'placeholder': 'Zip', 'class': 'form-control'}))
    phone_number = forms.CharField(required=True, min_length=1, max_length=100, label="Phone", widget=forms.TextInput(attrs={'placeholder': 'Phone', 'class': 'form-control'}))
    # is_staff = forms.BooleanField(required=True, label="Is Staff?", widget=forms.CheckboxInput)


##########################################################################
# shows the list of products
@view_function
def finalcheckout(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)

    params = {}

    try:
        user = hmod.User.objects.get(id=request.user.id)
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/accounts/')

    API_URL = 'http://dithers.cs.byu.edu/iscore/api/v1/charges'
    API_KEY = '9c37788a528e6f74ebd410d52e03a805'

    # create the form object
    # fill the form initially with data
    form = UserEditForm(initial={
        'cardtype': 'Visa',
        'cardname': 'Benjamin Willard',
        'cardnumber': '4732817300654',
        'cvc': '411',
        'expmonth': '10',
        'expyear': '15'
    })

    if request.method == 'POST':
        form = UserEditForm(request.POST)
        form.userid = user.id
        if form.is_valid():
            r = requests.post(API_URL, data={
            'apiKey': API_KEY,
            'currency': 'usd',
            'amount': '5.99',
            'type': 'Visa',
            'number': '4732817300654',
            'exp_month': '10',
            'exp_year': '15',
            'cvc': '411',
            'name': 'Cosmo Limesandal',
            'description': 'Charge for cosmo@is411.byu.edu',
            })

            print(r.text)

            resp = r.json()
            if 'error' in resp:
                print("<____________________________________________________________________________________________________________________________________________________________________________________>")
                print("ERROR: ", resp['error'])
                return HttpResponse('<script> window.location.href = "/homepage/checkout.finalcheckout" </script>')
            else:
                transaction = hmod.PaymentInfo()
                transaction.date = resp["Date"]
                transaction.description = resp["Description"]
                transaction.amount = resp["Amount"]
                transaction.transaction_id = resp["ID"]
                transaction.currency = resp["Currency"]
                transaction.customer = hmod.User.objects.get(id=user.id)
                transaction.save()
                return HttpResponse('<script> window.location.href = "/homepage/checkout.receipt" </script>')
                # print(resp.keys())
                # print(resp["ID"])

    # store the form in the parameters
    params['form'] = form
    params['user'] = user
    return templater.render_to_response(request, 'checkout.finalcheckout.html', params)


class UserEditForm(forms.Form):
    cardtype = forms.CharField(required=True, min_length=1, max_length=100, label="Card Type", widget=forms.TextInput(attrs={'placeholder': 'Card Type', 'class': 'form-control'}))
    cardname = forms.CharField(required=True, min_length=1, max_length=100, label="Name on Card", widget=forms.TextInput(attrs={'placeholder': 'Name on Card', 'class': 'form-control'}))
    cardnumber = forms.CharField(required=True, min_length=1, max_length=100, label="Credit Card Number", widget=forms.TextInput(attrs={'placeholder': 'Credit Card Number', 'class': 'form-control'}))
    cvc = forms.CharField(required=True, min_length=1, max_length=100, label="CVC Code", widget=forms.TextInput(attrs={'placeholder': 'CVC Code', 'class': 'form-control'}))
    expmonth = forms.CharField(required=True, min_length=1, max_length=100, label="Expiration Month", widget=forms.TextInput(attrs={'placeholder': 'Expiration Month', 'class': 'form-control'}))
    expyear = forms.CharField(required=True, min_length=1, max_length=100, label="Expiration Year", widget=forms.TextInput(attrs={'placeholder': 'Expiration Year', 'class': 'form-control'}))


##########################################################################
# shows the list of products
@view_function
def receipt(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)

    params = {}
    # send it back to the view
    pcart = request.session.get('pcart', {})
    icart = request.session.get('icart', {})
    products = {}
    items = {}
    amount = 0
    pamount = 0
    iamount = 0

# if item_type == "product":
    # loop through products to store in list
    for product in hmod.Product.objects.filter(id__in=pcart.keys()):
        products[str(product.id)] = product

    # loop through products to find total amount
    for key in products:
        p = products[key]
        amount += p.current_price * pcart[str(p.id)]

# elif item_type == "item":
    for item in hmod.Item.objects.filter(id__in=icart.keys()):
            items[str(item.id)] = item

    # loop through items to find total amount
    for key in items:
        i = items[key]
        iamount += i.standard_rental_price * icart[str(i.id)]    

    amount += iamount + pamount

    # load up params
    params = {
        'pcart': pcart,
        'icart': icart,
        'products': products,
        'items': items,
        'amount': amount,
    }


    useremail = request.user.email



    # send_mail('Receipt of Purchase', 'Thank you for your recent purchase.', settings.EMAIL_HOST_USER, [request.user.email], fail_silently=False)

    subject, from_email, to = 'Confirmation of Purchase', settings.EMAIL_HOST_USER, useremail
    text_content = 'This is an important message.'
    html_content = '''
      <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
      <html xmlns="http://www.w3.org/1999/xhtml">
      <head>
      <meta name="viewport" content="width=device-width" />
      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
      </head>
      <body>
        <hr>
        <p>Thank you for your recent purchase!  We appreciate your business.</p>
        <p>Your order will be sent within 5 business days.</p>
        <br>
        <br>
        <div class = "text-left">
      <h1>Thank You!</h1>
    </div>
    <p>Your purchase has been recorded and will be shipping soon!</p>
    <p>You have been sent an email with details of this transaction.</p>

    <form id= "loginform" method ="POST" action="/homepage/login.loginform/">
  <h1>Shopping Cart</h1>
    <table id="manage_table_shopping" class = "table table-striped table-bordered">
      <thead>
        <tr>
          <th>Photo</th>
          <th>Product Name</th>
          <th>Quantity</th>
          <th>Total</th>
        </tr>
      </thead>
      <tbody>
        {%for key in products: 
        <% p = products[key] %>
          <tr>
            <td><img class="text-center" height="75" src="${STATIC_URL}homepage/media/${ p.photo }" alt=""></td>
            <td>${ p.name }</td>
            <td>${ pcart[str(p.id)] }</td>
            <td>$ ${ p.current_price * pcart[str(p.id)] }</td>
          </tr>
        %endfor
      </tbody>
  </table>
  <table id="manage_table_shopping" class = "table table-striped table-bordered">
      <thead>
        <tr>
          <th>Photo</th>
          <th>Item Name</th>
          <th>Total</th>
        </tr>
      </thead>
      <tbody>
        %for key in items:
        <% i = items[key] %>
          <tr>
            <td><img class="text-center" height="75" src="${STATIC_URL}homepage/media/${ i.photo }" alt=""></td>
            <td>${ i.name }</td>
            <td>$ ${ i.standard_rental_price * icart[str(i.id)] }</td>
          </tr>
        %endfor
      </tbody>
  </table>

  <div id="Total" class="pull-right">
  <h4>Total Amount: $${ amount }</h4>
  </div>
    <div class="btn-group">
    </div>
  </form>
        <br>
        <p>The Founding Fathers</p>
        <br>
        <p> Having problems viewing this message?</p>
        <a href="http://localhost:8000/homepage/checkout.receipt/"><p>View Items Here</p></a>
      </html>
      '''
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    return templater.render_to_response(request, 'checkout.receipt.html', params)

