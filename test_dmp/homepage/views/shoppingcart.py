from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django.shortcuts import redirect
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth.models import check_password
from django.contrib.auth import authenticate, login, logout
import random


templater = get_renderer('homepage')


##########################################################################
# shows the list of users
@view_function
def process_request(request):

    params = {}
    # send it back to the view
    cart = request.session.get('cart', {})
    products = {}
    items = {}
    amount = 0

    # loop through products to store in list
    for product in hmod.Product.objects.filter(id__in=cart.keys()):
        products[str(product.id)] = product

    # loop through products to find total amount
    for key in products:
        p = products[key]
        pamount += p.current_price * cart[str(p.id)]

    # loop through products to store in list
    for item in hmod.Item.objects.filter(id__in=cart.keys()):
        items[str(item.id)] = item

    # loop through products to find total amount
    for key in items:
        i = items[key]
        iamount += i.standard_rental_price * cart[str(i.id)]    

    amount = iamount + pamount

    # load up params
    params = {
        'cart': cart,
        'products': products,
        'items': items,
        'amount': amount,
    }

    return templater.render_to_response(request, 'shoppingcart.form.html', params)


##########################################################################
# shows the list of users
@view_function
def add(request):

    params = {}

    # add to the shopping cart on button click
    # get the item for the shopping cart
    pid = request.urlparams[0]
    qty = request.urlparams[1]

    if pid and qty:
        # check to see if the shopping cart exists for this session, if not, add it.
        if 'cart' not in request.session:
            request.session['cart'] = {}

        # make shopping cart session a variable
        cart = request.session.get('cart', {})

        # check to see if the item is in the shopping cart, if it is, update the qty
        if pid in cart:
            # update the qty
            cart[pid] = int(cart[pid]) + int(qty)
        else:
            cart[pid] = int(qty)

        # save cart back to session
        request.session['cart'] = cart

        # get the product object
        p = hmod.Product.objects.get(id=pid)

        ##########################################################################
        # send it back to the view
        cart = request.session.get('cart', {})
        products = {}
        amount = 0

        # loop through products to store in list
        for product in hmod.Product.objects.filter(id__in=cart.keys()):
            products[str(product.id)] = product

        # loop through products to find total amount
        for key in products:
            p = products[key]
            amount += p.current_price * cart[str(p.id)]

        # load up params
        params = {
            'cart': cart,
            'products': products,
            'amount': amount,
        }
    else:
        #notify user to include a quantity
        return HttpResponseRedirect('/homepage/shoppingcart/')

    return templater.render_to_response(request, 'shoppingcart.html', params)


##########################################################################
# shows the list of users
@view_function
def delete(request):

    params = {}

    print(">>>>>>>>>>>>>>>>>>>>>>> about to delete stuff")
    # get the item for the shopping cart
    pid = request.urlparams[0]

    print(">>>>>>>>>>>>>>>>>>>>>>> delete = ", pid)

    value_to_remove = pid

    # get the cart from the session
    cart = request.session.get('cart', {})
    print(">>>>>>>>>>>>>>>>>>>>>>> cart before = ", cart)
    cart.pop(pid)

    # save cart back to session
    request.session['cart'] = cart
    print(">>>>>>>>>>>>>>>>>>>>>>> cart after = ", cart)

    # send it back to the view
    cart = request.session.get('cart', {})
    products = {}
    amount = 0

    # loop through products to store in list
    for product in hmod.Product.objects.filter(id__in=cart.keys()):
        products[str(product.id)] = product

    # loop through products to find total amount
    for key in products:
        p = products[key]
        amount += p.current_price * cart[str(p.id)]

    # load up params
    params = {
        'cart': cart,
        'products': products,
        'amount': amount,
    }

    # return HttpResponseRedirect('/homepage/productlist/')

    # this is the send it back in the ajax from but I haven't got that far yet.
    return templater.render_to_response(request, 'shoppingcart.form.html', params)
