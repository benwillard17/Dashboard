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
def process_request(request):
    #returns a form
   #go to the reset.html
##########################################################################
# shows the list of products
@view_function
def email(request):
        #get the userid(before I generate the token) and pass it as a param, so embed the param and token in email
        #generate a token and send in an email
    #send email and send back template

for customer in overdue_email:
        subject, from_email, to = 'NOTICE: Overdue Item', settings.EMAIL_HOST_USER, customer[4]
        text_content = 'This is an important message.'
        html_content = '''
          <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
          <html xmlns="http://www.w3.org/1999/xhtml">
          <head>
          <meta name="viewport" content="width=device-width" />
          <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
          </head>
          <body>
            <h1>Dear ''' + customer[2] + " " + customer[3] + '''!</h1>
            <hr>
            <p>Thank you for your recent purchase!  We appreciate your business.</p>
            <p>Your order will be sent within 5 business days.</p>
            <br>
            <br>
            SEND THE LOCALHOST LINK localhost:8000/homepage/reset.password/+token/+userid
            <br>
            <p>Colonial Heritage Team</p>
            <a href="http://www.cheritage.org/"><p>Colonial Heritage Foundation</p></a>
          </html>
          '''
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

###########################################################################
# edits a single account
@view_function
def password(request):

#grab the URL params, token and the ID
#use the ID to look up the user
#use the checker to check if it is correct(do that under if the form is valid and the passwords match)
#cast the token into a string once you've checked

    params = {}

    try:
        user = hmod.User.objects.get(id=request.urlparams[1])
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
            user = authenticate(username=username, password=request.POST['password1'])
            login(request, user)
            print('login user.')

            print('password changed.')
            return HttpResponseRedirect('/homepage/accounts/')
        return HttpResponseRedirect('/homepage/reset.password/{}/'.format(user.id))

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
def check_newpasswords(request):

    password1 = request.REQUEST.get('a')
    password2 = request.REQUEST.get('b')
    print('password1 = ', password1)
    print('password2 = ', password2)

    if password1 != password2:
        print('Passwords match!')
        return HttpResponse("0")
    return HttpResponse("1")