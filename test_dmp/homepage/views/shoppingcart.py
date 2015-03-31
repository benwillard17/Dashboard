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
    return templater.render_to_response(request, 'shoppingcart.form.html', params)


##########################################################################
# shows the list of users
@view_function
def add(request):

    params = {}

    # add to the shopping cart on button click
    # get the item for the shopping cart
    item_type = request.urlparams[2]
    if item_type == "product":
        pid = request.urlparams[0]
    elif item_type == "item":
        iid = request.urlparams[0]

    qty = request.urlparams[1]
    amount = 0
    pamount = 0
    iamount = 0

    pcart = request.session.get('pcart', {})
    icart = request.session.get('icart', {})

    if item_type == "product":
        if pid and qty:
            # check to see if the shopping cart exists for this session, if not, add it.
            if 'pcart' not in request.session:
                request.session['pcart'] = {}

            # make shopping cart session a variable
            pcart = request.session.get('pcart', {})

            # check to see if the item is in the shopping cart, if it is, update the qty
            if pid in pcart:
                # update the qty
                pcart[pid] = int(pcart[pid]) + int(qty)
            else:
                pcart[pid] = int(qty)

            # save cart back to session
            request.session['pcart'] = pcart
            if item_type == "product":
                # get the product object
                p = hmod.Product.objects.get(id=pid)
            elif item_type == "item":
                # get the product object
                i = hmod.Item.objects.get(id=iid)

            ##########################################################################
            # send it back to the view
            pcart = request.session.get('pcart', {})
            # for product in hmod.Product.objects.filter(id__in=pcart.keys()):
            #     products[str(product.id)] = product

            icart = request.session.get('icart', {})
            # for item in hmod.Item.objects.filter(id__in=icart.keys()):
            #     items[str(item.id)] = item

            products = {}
            items = {}
            amount = 0

        # if item_type == "product":
            # loop through products to store in list
            for product in hmod.Product.objects.filter(id__in=pcart.keys()):
                products[str(product.id)] = product

            # loop through products to find total amount
            for key in products:
                p = products[key]
                amount += p.current_price * pcart[str(p.id)]

        # elif item_type == "item":
            # loop through products to store in list
            for item in hmod.Item.objects.filter(id__in=icart.keys()):
                items[str(item.id)] = item

        # loop through items to find total amount
            for key in items:
                i = items[key]
                iamount += i.standard_rental_price * icart[str(i.id)]

    elif item_type == "item":
        if iid and qty:
            # check to see if the shopping cart exists for this session, if not, add it.
            if 'icart' not in request.session:
                request.session['icart'] = {}

            # make shopping cart session a variable
            icart = request.session.get('icart', {})

            # check to see if the item is in the shopping cart, if it is, update the qty
            if iid in icart:
                # update the qty
                icart[iid] = int(icart[iid]) + int(qty)
            else:
                icart[iid] = int(qty)

            # save cart back to session
            request.session['icart'] = icart
            if item_type == "product":
                # get the product object
                p = hmod.Product.objects.get(id=pid)
            # elif item_type == "item":
            #     # get the product object
            #     i = hmod.Item.objects.get(id=pid)

            ##########################################################################
            # send it back to the view
            pcart = request.session.get('pcart', {})
            # for product in hmod.Product.objects.filter(id__in=pcart.keys()):
            #     products[str(product.id)] = product

            icart = request.session.get('icart', {})
            # for item in hmod.Item.objects.filter(id__in=icart.keys()):
            #     items[str(item.id)] = item

            products = {}
            items = {}
            amount = 0

        # if item_type == "product":
            # loop through products to store in list
            for product in hmod.Product.objects.filter(id__in=pcart.keys()):
                products[str(product.id)] = product

            # loop through products to find total amount
            for key in products:
                p = products[key]
                amount += p.current_price * pcart[str(p.id)]

        # elif item_type == "item":
            # loop through products to store in list
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

    return templater.render_to_response(request, 'shoppingcart.html', params)


##########################################################################
# shows the list of users
@view_function
def delete(request):

    params = {}

    item_type = request.urlparams[1]
    if item_type == "product":
        pid = request.urlparams[0]
        value_to_remove = pid
        pcart = request.session.get('pcart', {})
        pcart.pop(pid)
        # save cart back to session
        request.session['pcart'] = pcart
    elif item_type == "item":
        iid = request.urlparams[0]
        value_to_remove = iid
        # get the cart from the session
        icart = request.session.get('icart', {})
        icart.pop(iid)
        # save cart back to session
        request.session['icart'] = icart

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

    # return HttpResponseRedirect('/homepage/productlist/')

    # this is the send it back in the ajax from but I haven't got that far yet.
    return templater.render_to_response(request, 'shoppingcart.form.html', params)
