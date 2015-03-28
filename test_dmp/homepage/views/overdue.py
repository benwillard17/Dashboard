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
from django.db import connection, connections
import time
import datetime
from django.core.mail import EmailMultiAlternatives


templater = get_renderer('homepage')


@view_function
def process_request(request):

    params = {}
    cursor = connection.cursor()
    date = time.strftime("%Y/%m/%d")
    start_date = datetime.datetime.strptime(date, "%Y/%m/%d")
    thirty = (start_date - datetime.timedelta(days=30)).strftime("%Y/%m/%d")
    sixty = (start_date - datetime.timedelta(days=60)).strftime("%Y/%m/%d")
    ninety = (start_date - datetime.timedelta(days=90)).strftime("%Y/%m/%d")


    cursor.execute('''
    SELECT 
      homepage_item.name, 
      homepage_rental.due_date, 
      homepage_user.first_name, 
      homepage_user.last_name, 
      homepage_user.email
    FROM 
      public.homepage_rental, 
      public.homepage_rentalitem, 
      public.homepage_user, 
      public.homepage_item
    WHERE 
      homepage_rental.rentee_id = homepage_user.id AND
      homepage_rentalitem.rental_id = homepage_rental.id AND
      homepage_item.id = homepage_rentalitem.item_id AND
      homepage_rental.due_date < %s and homepage_rental.due_date > %s AND
      homepage_rentalitem.returned = FALSE
     ORDER BY
      homepage_rental.due_date ASC;''', ([thirty, sixty]))
    overdue1 = cursor.fetchall()

    cursor.execute('''
    SELECT 
      homepage_item.name, 
      homepage_rental.due_date, 
      homepage_user.first_name, 
      homepage_user.last_name, 
      homepage_user.email
    FROM  
      public.homepage_rental, 
      public.homepage_rentalitem, 
      public.homepage_user, 
      public.homepage_item
    WHERE 
      homepage_rental.rentee_id = homepage_user.id AND
      homepage_rentalitem.rental_id = homepage_rental.id AND
      homepage_item.id = homepage_rentalitem.item_id AND
      homepage_rental.due_date < %s and homepage_rental.due_date > %s AND
      homepage_rentalitem.returned = FALSE
     ORDER BY
      homepage_rental.due_date ASC;''', ([sixty, ninety]))
    overdue2 = cursor.fetchall()

    cursor.execute('''
    SELECT 
      homepage_item.name, 
      homepage_rental.due_date, 
      homepage_user.first_name, 
      homepage_user.last_name, 
      homepage_user.email
    FROM 
      public.homepage_rental, 
      public.homepage_rentalitem, 
      public.homepage_user, 
      public.homepage_item
    WHERE 
      homepage_rental.rentee_id = homepage_user.id AND
      homepage_rentalitem.rental_id = homepage_rental.id AND
      homepage_item.id = homepage_rentalitem.item_id AND
      homepage_rental.due_date < %s AND
      homepage_rentalitem.returned = FALSE
     ORDER BY
      homepage_rental.due_date ASC;''', ([ninety]) )
    overdue3 = cursor.fetchall()


    params['overdue1'] = overdue1
    params['overdue2'] = overdue2
    params['overdue3'] = overdue3

    return templater.render_to_response(request, 'overdue.html', params)

@view_function
def email(request):

    params = {}

    cursor = connection.cursor()
    cursor.execute('''
    SELECT 
      homepage_item.name, 
      homepage_rental.due_date, 
      homepage_user.first_name, 
      homepage_user.last_name, 
      homepage_user.email,
      homepage_rental.id
    FROM 
      public.homepage_rental, 
      public.homepage_rentalitem, 
      public.homepage_user, 
      public.homepage_item
    WHERE 
      homepage_rental.rentee_id = homepage_user.id AND
      homepage_rentalitem.rental_id = homepage_rental.id AND
      homepage_item.id = homepage_rentalitem.item_id AND
      homepage_rentalitem.returned = FALSE ''')
    emaillist = cursor.fetchall()


    for user in emaillist:
        subject, from_email, to = 'NOTICE: Overdue Item: ' + user[0], settings.EMAIL_HOST_USER, user[4]
        text_content = 'This is an important message.'
        html_content = '''
          <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
          <html xmlns="http://www.w3.org/1999/xhtml">
          <head>
          <meta name="viewport" content="width=device-width" />
          <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
          </head>
          <body>
            <h1>Dear ''' + user[2] + " " + user[3] + '''!</h1>
            <hr>
            <p></p>
            <p></p>
            <br>
            <br>
            <br>
            <p>The Founding Fathers</p>
            <a href="http://www.cheritage.org/"><p>Colonial Heritage Foundation</p></a>
          </html>
          '''
        emailmessage = EmailMultiAlternatives(subject, text_content, from_email, [to])
        emailmessage.attach_alternative(html_content, "text/html")
        emailmessage.send()

    params['emaillist'] = emaillist

    return templater.render_to_response(request, 'success.html', params)
