from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django.contrib.auth import authenticate, login
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from ldap3 import Server, Connection, AUTH_SIMPLE, STRATEGY_SYNC, STRATEGY_ASYNC_THREADED, SEARCH_SCOPE_WHOLE_SUBTREE, GET_ALL_INFO


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
            try:
                domain = 'CHERITAGE\\'
                username = self.cleaned_data['username']
                pw = self.cleaned_data['password']
                print("try user is in AD")
                s = Server('128.187.61.39', port=8889, get_info=GET_ALL_INFO)
                c = Connection(s, auto_bind=True, client_strategy=STRATEGY_SYNC, user=domain+username, password=pw, authentication=AUTH_SIMPLE)
                u, created = hmod.User.objects.get_or_create(username=username)
                u.first_name = username
                u.last_name = ''
                u.email = username+'@cheritage.org'
                u.set_password(pw)
                u.is_staff = True
                u.is_active = True
                u.is_super_user = False
                u.save()
                user = authenticate(username=username, password=pw)
            except:
                print("not in ad try in django")
                print("wat's up asdfio")
                user = authenticate(username=username, password=pw)
            if user is None:
                print("is my user nobody?")
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
            domain = 'CHERITAGE\\'
            username = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            try:
                s = Server('128.187.61.39', port=8889, get_info=GET_ALL_INFO)
                c = Connection(s, auto_bind=True, client_strategy = STRATEGY_SYNC,
                    user=domain+username,
                    password=pw, authentication=AUTH_SIMPLE
                    )
                print(c)

                u, created = hmod.User.objects.get_or_create(username=username)
                u.first_name = username
                u.last_name = ''
                u.email = username+'@cheritage.org'
                u.set_password(pw)
                u.is_staff = True
                u.is_active = True
                u.is_super_user = False
                u.save()

                u2 = authenticate(username, pw)
                login(request, u2)


            except:
                print("wat's up asdfio")
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

