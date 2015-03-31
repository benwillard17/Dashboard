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
import requests

API_URL = 'http://dithers.cs.byu.edu/iscore/api/v1/charges'
API_KEY = '9c37788a528e6f74ebd410d52e03a805'


##########################################################################
# shows the list of users
@view_function
def charge_credit_card(request):
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

    resp=r.json()
    if 'error' in resp:
        print("ERROR: ", resp ['error'])
    else:
        print(resp.keys())
        print(resp["ID"])
