from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django.shortcuts import redirect
from django_mako_plus.controller.router import get_renderer


templater = get_renderer('homepage')


##########################################################################
# shows the list of products
@view_function
def process_request(request):


    ###send them to the modal to login
    #maybe make a special page with create account option

    return redirect('/homepage/login/?next=%s' % request.path)

    params = {}

    ###form to put in info
    form = Checktheheckoutform(initial={
        'credit_card': '',
        'address': '',
        'city': '',
        'state': '',
        'country': '',
        'zipcode': '',
    })
    if request.method == 'POST':
        form = Checktheheckoutform(request.POST)
            return HttpResponseRedirect('/homepage/checkoureceipt/')

    # store the form in the parameters
    params['form'] = form
    params['product'] = product
    return templater.render_to_response(request, 'checkout.edit.html', params)


class Checktheheckoutform(forms.Form):
    category = forms.CharField(required=True, label="Category", widget=forms.TextInput(attrs={'placeholder': 'Category', 'class': 'form-control'}))
    current_price = forms.DecimalField(required=True, label="Current Price", widget=forms.TextInput(attrs={'placeholder': 'Current Price', 'class': 'form-control'}))
    producer_name = forms.CharField(required=False, min_length=1, max_length=15, label="Producer Name", widget=forms.TextInput(attrs={'placeholder': 'Producer Name', 'class': 'form-control'}))



# ##########################################################################
# # create a new product
# @view_function
# def create(request):
#     if not request.user.is_authenticated():
#         return redirect('/homepage/login/?next=%s' % request.path)
#     if not request.user.is_staff:
#         return HttpResponseRedirect('/homepage/authentication')

#     '''Creates a new product'''
#     product = hmod.Product()
#     product.category = ''
#     # product.current_price = ''
#     product.producer_name = ''
#     product.save()

#     return HttpResponseRedirect('/homepage/checkout.edit/{}/'.format(product.id))



