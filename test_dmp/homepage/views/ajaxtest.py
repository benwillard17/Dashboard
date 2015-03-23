from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django.contrib.auth import authenticate, login
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer


templater = get_renderer('homepage')


###########################################################################
# edits a single user
@view_function
def process_request(request):
    params ={}

    form = LoginForm()
    # if request.method == 'POST'
      form = LoginForm(request.POST)
      if form.is_valid():
        # do something here. (Authenticate and Login)

    params['form'] = form
    return templater.render_to_response(request, 'ajaxtest.html', params)


class LoginForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField()


###########################################################################
# check the username
@view_function
def check_username(request):

    # get the username from the server
    # using a dictionary
    username = request.REQUEST.get['u']
    password = request.REQUEST.get['p']
    print('>>>>>>>>>>>>>>>>>>>', username)

    user = hmod.User.objects.get(username=username)

    #check that username exists, and does it exist with a different username than the current user
    #if its good
    return HttpResponse("1")
    #if its bad
    return HttpResponse("0")
