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
    params = {}

    return templater.render_to_response(request, 'login.html', params)


class LoginForm(forms.Form):
    username = forms.CharField(label=('Username'), widget=forms.TextInput())
    password = forms.CharField(label=('Password'), widget=forms.PasswordInput())

    def clean(self):
        if len(self.errors) == 0:
            user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
            if user is None:
                raise forms.ValidationError('Invalid Username or Password')


###########################################################################
# edits a single user
@view_function
def loginform(request):
    params = {}

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponse('<script> window.location.href = "/homepage/index" </script>')

    params['form'] = form
    return templater.render_to_response(request, 'login.loginform.html', params)


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


###################################################
# if you have to change a file, these are all related.
# login.py
# login.html

# base.htm - button for the login
# base.js

# login.loginform.html
# login.loginform.js

