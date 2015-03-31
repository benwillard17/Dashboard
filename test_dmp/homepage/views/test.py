import requests


API_URL = 'http://dithers.cs.byu.edu/iscore/api/v1/charges'
API_KEY = '9c37788a528e6f74ebd410d52e03a805'

# # create the form object
# # fill the form initially with data
# form = UserEditForm(initial={
#     'cardtype': '',
#     'cardname': '',
#     'cardnumber': '',
#     'cvc': '',
#     'expmonth': '',
#     'expyear': ''
# })



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

resp = r.json()
if 'error' in resp:
    print("<____________________________________________________________________________________________________________________________________________________________________________________>")
    print("ERROR: ", resp['error'])
#     return HttpResponse('<script> window.location.href = "/homepage/checkout.finalcheckout" </script>')


print(r.text)

# # store the form in the parameters
# params['form'] = form
# params['user'] = user
# return templater.render_to_response(request, 'checkout.receipt.html', params)


# class UserEditForm(forms.Form):
# cardtype = forms.CharField(required=True, min_length=1, max_length=100, label="Card Type", widget=forms.TextInput(attrs={'placeholder': 'Card Type', 'class': 'form-control'}))
# cardname = forms.CharField(required=True, min_length=1, max_length=100, label="Name on Card", widget=forms.TextInput(attrs={'placeholder': 'Name on Card', 'class': 'form-control'}))
# cardnumber = forms.CharField(required=True, min_length=1, max_length=100, label="Credit Card Number", widget=forms.TextInput(attrs={'placeholder': 'Credit Card Number', 'class': 'form-control'}))
# cvc = forms.CharField(required=True, min_length=1, max_length=100, label="CVC Code", widget=forms.TextInput(attrs={'placeholder': 'CVC Code', 'class': 'form-control'}))
# expmonth = forms.CharField(required=True, min_length=1, max_length=100, label="Expiration Month", widget=forms.TextInput(attrs={'placeholder': 'Expiration Month', 'class': 'form-control'}))
# expyear = forms.CharField(required=True, min_length=1, max_length=100, label="Expiration Year", widget=forms.TextInput(attrs={'placeholder': 'Expiration Year', 'class': 'form-control'}))

