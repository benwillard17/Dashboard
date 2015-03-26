from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django.shortcuts import redirect
import random


templater = get_renderer('homepage')


##########################################################################
# shows the list of events
@view_function
def process_request(request):

    params = {}

    events = hmod.Event.objects.all().order_by('id')
    params['events'] = events

    return templater.render_to_response(request, 'festivals.html', params)


###########################################################################
# edits a single event
@view_function
def view(request):

    params = {}

    try:
        events = hmod.Event.objects.get(id=request.urlparams[0])
    except hmod.Event.DoesNotExist:
        return HttpResponseRedirect('/homepage/festivals/')

    areas = hmod.Area.objects.all()

    params['events'] = events
    params['areas'] = areas
    return templater.render_to_response(request, 'festivals.view.html', params)

@view_function
def area(request):

    params = {}

    try:
        areas = hmod.Area.objects.get(id=request.urlparams[0])
    except hmod.Area.DoesNotExist:
        return HttpResponseRedirect('/homepage/festivals')

    areas = hmod.Area.objects.all()
    products = hmod.Product.objects.all()

    params['areas'] = areas
    params['products'] = products
    return templater.render_to_response(request, 'festivals.area.html', params)
  