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

templater = get_renderer('homepage')


##########################################################################
# shows the list of products
@view_function
def password_change_form(request):
    params = {}

    try:
        user = hmod.User.objects.get(id=request.user.id)
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/accounts/')

    # create the form object
    # fill the form initially with data
    form = {}
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        form.userid = user.id
        if form.is_valid():
            return HttpResponse('<script> window.location.href = "/homepage/views.password_reset_done" </script>')

    # store the form in the parameters
    params['form'] = form
    params['user'] = user
    return templater.render_to_response(request, 'views.password_reset_done.html', params)


class PasswordResetForm(forms.Form):
    username = forms.CharField(required=True, min_length=1, max_length=100, label="Username", widget=forms.TextInput(attrs={'placeholder': 'UserName', 'class': 'form-control'}))


class ResetPasswordRequestView(FormView):
    template_name = "account/test_template.html"    #code for template is given below the view's code
    success_url = '/account/login'
    form_class = PasswordResetRequestForm

   

##########################################################################
# shows the list of products
@view_function
def finalcheckout(request):

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
        'cardtype': '',
        'cardname': '',
        'cardnumber': '',
        'cvc': '',
        'expmonth': '',
        'expyear': ''
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
                # print(resp.keys())
                # print(resp["ID"])

    # store the form in the parameters
    params['form'] = form
    params['user'] = user
    return templater.render_to_response(request, 'checkout.receipt.html', params)


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

    useremail = request.user.email

    send_mail('Receipt of Purchase', 'Thank you for your recent purchase.', settings.EMAIL_HOST_USER, [request.user.email], fail_silently=False)

    return templater.render_to_response(request, 'receipt.html', params)



######################################################################
@view_function
def charge_credit_card(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)
    if not request.user.is_staff:
        return HttpResponseRedirect('/homepage/authentication')

    params = {}

    try:
        user = hmod.User.objects.get(id=request.urlparams[0])
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/accounts/')

    # create the form object
    # fill the form initially with data
    form = UserEditForm(initial={
        'username': user.username,
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
        form = UserEditForm(request.POST)
        form.userid = user.id
        if form.is_valid():
            # make the changes on the user object
            user.username = form.cleaned_data['username']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.address1 = form.cleaned_data['address1']
            user.address2 = form.cleaned_data['address2']
            user.city = form.cleaned_data['city']
            user.state = form.cleaned_data['state']
            user.zipcode = form.cleaned_data['zipcode']
            user.phone_number = form.cleaned_data['phone_number']
            user.save()
            return HttpResponseRedirect('/homepage/accounts/')

    # store the form in the parameters
    params['form'] = form
    params['user'] = user
    return templater.render_to_response(request, 'accounts.edit.html', params)


class UserEditForm(forms.Form):
    username = forms.CharField(required=True, min_length=1, max_length=100, label="Username", widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
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

    def clean_username(self):
        # check if the username is more than 6
        if len(self.cleaned_data['username']) < 3:
            raise forms.ValidationError('Please enter a username that is at least 3 characters.')

        # check to see the username already exists
        user_count = hmod.User.objects.filter(username=self.cleaned_data['username']).exclude(id=self.userid).count()
        if user_count >= 1:
            raise forms.ValidationError("This username is already taken")

        return self.cleaned_data['username']



###########################################################################
# edits a single account
@view_function
def password(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)
    if not request.user.is_staff:
        return HttpResponseRedirect('/homepage/authentication')

    params = {}

    try:
        user = hmod.User.objects.get(id=request.urlparams[0])
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/accounts/')

    # create the form object
    # fill the form initially with data
    form = UserPasswordEdit(initial={
        'password1': '',
        'password2': '',
    })
    if request.method == 'POST':
        form = UserPasswordEdit(request.POST)
        form.userid = user.id
        if request.POST['password1'] == request.POST['password2']:
            print('New passwords match.')
            # set the password
            request.user.set_password(request.POST['password1'])
            request.user.save()
            print('user saved')
            username = request.user.username
            logout(request)
            print('logout user')
            user = authenticate(username=username, password=request.POST['password1'])
            login(request, user)
            print('login user.')

            print('password changed.')
            return HttpResponseRedirect('/homepage/accounts/')
        return HttpResponseRedirect('/homepage/accounts.password/{}/'.format(user.id))

    # store the form in the parameters
    params['form'] = form
    params['user'] = user
    return templater.render_to_response(request, 'accounts.password.html', params)


class UserPasswordEdit(forms.Form):
    password1 = forms.CharField(label="New Password", widget=forms.TextInput())
    password2 = forms.CharField(label="Re-Enter New Password", widget=forms.TextInput())

    # def clean_data(self):
    #     # check if the username is more than 6
    #     if len(self.cleaned_data['cpassword']) < 6:
    #         raise forms.ValidationError('Please enter a username that is at least 3 characters.')
    #     return self.cleaned_data['cpassword']


###########################################################################
# check the username
@view_function
def check_currentpassword(request):

    print('you made it to the server - current password')
    cpassword = request.REQUEST.get('a')
    print('cpassword = ', cpassword)
    valid = request.user.check_password(cpassword)
    if valid is True:
        print('User entered current password correctly')
        return HttpResponse("1")
    return HttpResponse("0")


###########################################################################
# check the username
@view_function
def check_newpasswords(request):

    password1 = request.REQUEST.get('a')
    password2 = request.REQUEST.get('b')
    print('password1 = ', password1)
    print('password2 = ', password2)

    if password1 != password2:
        print('Passwords match!')
        return HttpResponse("0")
    return HttpResponse("1")