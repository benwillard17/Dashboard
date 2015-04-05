from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django.shortcuts import redirect
import random
from django.db import connection, connections
import time
import datetime

templater = get_renderer('homepage')


##########################################################################
# shows the list of areas
@view_function
def process_request(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)
    if not request.user.is_staff:
        return HttpResponseRedirect('/homepage/authentication')

    params = {}
    cursor = connection.cursor()
    # date = time.strftime("%Y/%m/%d")
    # start_date = datetime.datetime.strptime(date, "%Y/%m/%d")
    # thirty = (start_date - datetime.timedelta(days=30)).strftime("%Y/%m/%d")
    # sixty = (start_date - datetime.timedelta(days=60)).strftime("%Y/%m/%d")
    # ninety = (start_date - datetime.timedelta(days=90)).strftime("%Y/%m/%d")

    cursor.execute('''
    SELECT 
      homepage_user.last_name, 
      homepage_user.first_name, 
      homepage_user.email,
      homepage_item.name, 
      homepage_rental.due_date, 
      homepage_rentalitem.id
    FROM 
      public.homepage_rental, 
      public.homepage_rentalitem, 
      public.homepage_user, 
      public.homepage_item
    WHERE 
      homepage_rental.rentee_id = homepage_user.id AND
      homepage_rentalitem.rental_id = homepage_rental.id AND
      homepage_item.id = homepage_rentalitem.item_id AND
      homepage_rentalitem.returned = FALSE
     ORDER BY
      homepage_user.last_name;''')
    returns = cursor.fetchall()

    params['returns'] = returns

    return templater.render_to_response(request, 'return.html', params)


###########################################################################
# edits a single rental
@view_function
def edit(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)
    if not request.user.is_staff:
        return HttpResponseRedirect('/homepage/authentication')

    '''Creates a new return'''
    returns = hmod.Return()
    returns.save()

    params = {}

    try:
        rentalitem = hmod.RentalItem.objects.get(id=request.urlparams[0])
    except hmod.RentalItem.DoesNotExist:
        return HttpResponseRedirect('/homepage/return/')

    try:
        returns = hmod.Return.objects.get(id=rentalitem.id)
    except hmod.Return.DoesNotExist:
        returns = hmod.Return()
        returns.save()

    # create the form object
    # fill the form initially with data
    form = RentalItemEditForm(initial={
        'condition': rentalitem.condition,
        'new_damage': rentalitem.new_damage,
        'damage_fee': rentalitem.damage_fee,
        'late_fee': rentalitem.late_fee,
        'fees_paid': returns.fees_paid,
        'fees_waived': returns.fees_waived,
    })
    if request.method == 'POST':
        form = RentalItemEditForm(request.POST)
        form.rentalitemid = rentalitem.id
        if form.is_valid():
            # make the changes on the rentalitem object
            rentalitem.condition = form.cleaned_data['condition']
            rentalitem.new_damage = form.cleaned_data['new_damage']
            rentalitem.damage_fee = form.cleaned_data['damage_fee']
            rentalitem.late_fee = form.cleaned_data['late_fee']
            rentalitem.returned = True
            rentalitem.rental_return = hmod.Return.objects.get(id=returns.id)
            rentalitem.save()
            returns.time = datetime.datetime.now()
            returns.fees_paid = form.cleaned_data['fees_paid']
            returns.fees_waived = form.cleaned_data['fees_waived']
            returns.agent = hmod.User.objects.get(id=request.user.id)

            returns.save()

            return HttpResponseRedirect('/homepage/return/')

    # store the form in the parameters
    params['form'] = form
    params['rentalitem'] = rentalitem
    return templater.render_to_response(request, 'return.edit.html', params)


class RentalItemEditForm(forms.Form):
    condition = forms.CharField(required=True, min_length=1, max_length=100, label="Condition", widget=forms.TextInput(attrs={'placeholder': 'Condition', 'class': 'form-control'}))
    new_damage = forms.BooleanField(required=False, label="New Damage", widget=forms.CheckboxInput())
    damage_fee = forms.DecimalField(required=True, label="Damage Fee", widget=forms.TextInput(attrs={'placeholder': 'Damage Fee', 'class': 'form-control'}))
    late_fee = forms.DecimalField(required=True, label="Late Fee", widget=forms.TextInput(attrs={'placeholder': 'Late Fee', 'class': 'form-control'}))
    fees_paid = forms.BooleanField(required=False, label="Fees Paid", widget=forms.CheckboxInput())
    fees_waived = forms.BooleanField(required=False, label="Fees Waived", widget=forms.CheckboxInput())

    # def clean_data(self):
    #     # check if the zip is not 5
    #     if len(self.cleaned_data['place_number']) < 3:
    #         raise forms.ValidationError('Invalid number.')

    #     return self.cleaned_data['place_number']


##########################################################################
# create a new area
@view_function
def create(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)
    if not request.user.is_staff:
        return HttpResponseRedirect('/homepage/authentication')

    '''Creates a new area'''
    area = hmod.Area()
    area.name = ''
    area.description = ''
    area.place_number = ''
    # area.event = ''
    area.save()

    return HttpResponseRedirect('/homepage/areas.edit/{}/'.format(area.id))


##########################################################################
# delete a new area
@view_function
def delete(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)
    if not request.user.is_staff:
        return HttpResponseRedirect('/homepage/authentication')
    '''Delete a area'''
    try:
        area = hmod.Area.objects.get(id=request.urlparams[0])
    except hmod.Area.DoesNotExist:
        return HttpResponseRedirect('/homepage/areas/')

    area.delete()
    return HttpResponseRedirect('/homepage/areas/')
