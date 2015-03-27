from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django.shortcuts import redirect
from django_mako_plus.controller.router import get_renderer

templater = get_renderer('homepage')



##########################################################################
# shows the list of items
@view_function
def process_request(request):
    params = {}

    items = hmod.Item.objects.all()
    params['items'] = items

    return templater.render_to_response(request, 'itemlist.html', params)

###########################################################################
# edits a single item
@view_function
def viewitem(request):

    params = {}
    try:
        item = hmod.Item.objects.get(id=request.urlparams[0])
    except hmod.Item.DoesNotExist:
        return HttpResponseRedirect('/homepage/itemlist/')

    params['item'] = item
    return templater.render_to_response(request, 'itemlist.viewitem.html', params)


class ItemEditForm(forms.Form):

    name = forms.CharField(required=True, label="Category", widget=forms.TextInput(attrs={'placeholder': 'Category', 'class': 'form-control'}))
    standard_rental_price = forms.DecimalField(required=True, label="Current Price", widget=forms.TextInput(attrs={'placeholder': 'Current Price', 'class': 'form-control'}))
    owner = forms.CharField(required=False, min_length=1, max_length=15, label="Producer Name", widget=forms.TextInput(attrs={'placeholder': 'Producer Name', 'class': 'form-control'}))

    def clean_data(self):
        # check if the made_to_item_items is not 5
        if len(self.cleaned_data['standard_rental_price']) > 10:
            raise forms.ValidationError('Invalid price.')

        return self.cleaned_data['standard_rental_price']