from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django.shortcuts import redirect
from django_mako_plus.controller.router import get_renderer

templater = get_renderer('homepage')

@view_function
def process_request(request):


    params = {}

    return templater.render_to_response(request, 'shopping_cart.html', params)

@view_function
def add(request):
	if 'shopping_cart' not in request.session:
		request.session['shopping_cart'] = {}

	pid = request.urlparams[0]
	qty = request.urlparams[1]

	if pid in request.session['shopping_cart']:
		request.session['shopping_cart'][pid] += qty
	else:
		request.session['shopping_cart'][pid] = qty

	return HttpResponseRedirect('/homepage/shopping_cart')