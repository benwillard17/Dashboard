#!/usr/bin/env python3
# this allows unix to recognize the program.

# initialize django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'test_dmp.settings'
import django
django.setup()

from django.contrib.auth import models as conmod
import homepage.models as hmod

# regular imports
import random, re
from django import forms
import homepage.models as hmod


# empty (or drop) the tables


# create some users
u = hmod.User()
u.first_name = "Conan"
u.last_name = "Albrecht"
u.set_password = "i8adog"
u.username = 'u1'
u.is_superuser = True
u.save()


g = Group()
# ....
g.save()
g.add_user(u)



##### LIDDLE
for data in [
  ["Conan","Albrecht"],
]:

u = hmod.User()
u.first_name = data[0]
u.last_name = "Albrecht"
u.set_password = "i8adog"
u.username = 'u1'
u.is_superuser = True
u.save()


#####ALBRECHT
for data in [
  {'first_name': 'Conan', 'first_name': 'Albrecht'}
]:

u = hmod.User()
for k, v in data.items():
    setattr(u, k, v)
u.save()
