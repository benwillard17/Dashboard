import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'test_dmp.settings'
import django; django.setup()
from django.contrib.auth import models as conmod
import homepage.models as hmod
from django.contrib.auth.models import Group, Permission, ContentType

# populating data for photographs
for data in [
    {'date_taken': '2001-1-1', 'place_taken': 'Russia', 'description': 'photo1', 'image': 'photo1.jpg'},
    {'date_taken': '2002-2-2', 'place_taken': 'Japan', 'description': 'photo2', 'image': 'photo2.jpg'},
    {'date_taken': '2003-3-3', 'place_taken': 'France', 'description': 'photo3', 'image': 'photo3.jpg'},
    {'date_taken': '2004-4-4', 'place_taken': 'Mexico', 'description': 'photo4', 'image': 'photo4.jpg'},
    {'date_taken': '2005-5-5', 'place_taken': 'Germany', 'description': 'photo5', 'image': 'photo5.jpg'},
]:

    d = hmod.Photograph()
    for k, v in data.items():
        setattr(d, k, v)
    d.save()

# Create Super Group, Permissions, and User
permission = Permission()
permission.codename = 'super'
permission.content_type = ContentType.objects.get(id=7)
permission.name = 'Super Privileges'
permission.save()

group = Group()
group.name = "super"
group.save()
group.permissions.add(permission)
permission = Permission.objects.get(id=61)
group.permissions.add(permission)

user = hmod.User()
user.is_staff = 'True'
user.is_active = 'True'
user.is_superuser = 'True'
user.username = 'super'
user.set_password('asdf')
user.first_name = 'Super'
user.last_name = 'User'
user.email = 'super@cheritage.org'
user.address1 = '4387 South 1400 East'
user.address2 = ''
user.city = 'Sandy'
user.state = 'Utah'
user.zipcode = '84118'
user.phone_number = '8015558765'
user.security_question = 'What is your favorite color?'
user.security_answer = 'green'
user.emergency_contact = 'Jackson Murdock'
user.emergency_phone = '8015556543'
user.emergency_relationship = 'Friend'
user.id_photo = hmod.Photograph.objects.get(id=1)
user.organization_name = ''
user.save()

group.user_set.add(user)


# Create Staff Group, Permissions, and User
permission = Permission()
permission.codename = 'staff'
permission.content_type = ContentType.objects.get(id=7)
permission.name = 'Staff Privileges'
permission.save()

group = Group()
group.name = "staff"
group.save()
group.permissions.add(permission)
permission = Permission.objects.get(id=62)
group.permissions.add(permission)

user = hmod.User()
user.is_staff = 'True'
user.is_active = 'True'
user.is_superuser = 'False'
user.username = 'staff'
user.set_password('asdf')
user.first_name = 'Staff'
user.last_name = 'User'
user.email = 'staff@cheritage.org'
user.address1 = '1300 East 400 North'
user.address2 = ''
user.city = 'Logan'
user.state = 'Utah'
user.zipcode = '84708'
user.phone_number = '4356897732'
user.security_question = 'What is your favorite color?'
user.security_answer = 'blue'
user.emergency_contact = 'Luis Mark'
user.emergency_phone = '8016751234'
user.emergency_relationship = 'Friend'
user.id_photo = hmod.Photograph.objects.get(id=1)
user.organization_name = ''
user.save()

group.user_set.add(user)


# Create Guest Group, Permissions, and User
permission = Permission()
permission.codename = 'guest'
permission.content_type = ContentType.objects.get(id=7)
permission.name = 'Guest Privileges'
permission.save()

group = Group()
group.name = "guest"
group.save()
group.permissions.add(permission)
permission = Permission.objects.get(id=63)
group.permissions.add(permission)


user = hmod.User()
user.is_staff = 'False'
user.is_active = 'True'
user.is_superuser = 'False'
user.username = 'guest'
user.set_password('asdf')
user.first_name = 'Guest'
user.last_name = 'User'
user.email = 'guest@cheritage.org'
user.address1 = '5534 Youth Street'
user.address2 = ''
user.city = 'Hyrum'
user.state = 'Utah'
user.zipcode = '84704'
user.phone_number = '4356872334'
user.security_question = 'What is your favorite color?'
user.security_answer = 'purple'
user.emergency_contact = 'Andy Rawlings'
user.emergency_phone = '8019875623'
user.emergency_relationship = 'Friend'
user.id_photo = hmod.Photograph.objects.get(id=1)
user.organization_name = ''
user.save()

group.user_set.add(user)


# populating data for users
for data in [
    {'is_staff': 'True', 'is_active': 'True', 'is_superuser': 'True', 'username': 'CHF', 'set_password': 'asdf', 'first_name': 'Colonial', 'last_name': 'Heritage', 'email': 'kbj17.me@gmail.com', 'address': '1234 North Center Street', 'city': 'Lehi', 'state': 'Utah', 'zipcode': '84604', 'phone_number': '4443334444', 'security_question': 'Am I who I say I am?', 'security_answer': 'Yes', 'emergency_contact': 'Fred', 'emergency_phone': '911', 'emergency_relationship': 'Doctor'},
    {'is_staff': 'True', 'is_active': 'True', 'is_superuser': 'False', 'username': 'ben17', 'set_password': 'asdf', 'first_name': 'Ben', 'last_name': 'Willard', 'email': 'kbj17.me@gmail.com', 'address': 'North Circle', 'city': 'Provo', 'state': 'Utah', 'zipcode': '84604', 'phone_number': '4445554444', 'security_question': 'Am I who I say I am?', 'security_answer': 'Yes', 'emergency_contact': 'Bob', 'emergency_phone': '911', 'emergency_relationship': 'Doctor'},
    {'is_staff': 'True', 'is_active': 'True', 'is_superuser': 'False', 'username': 'taylor', 'set_password': 'asdf', 'first_name': 'Taylor', 'last_name': 'Curtis', 'email': 'tcurtistest@gmail.com', 'address': 'GW Boulevard', 'city': 'Salt Lake City', 'state': 'Utah', 'zipcode': '84604', 'phone_number': '4446662222', 'security_question': 'Am I who I say I am?', 'security_answer': 'Yes', 'emergency_contact': 'Fred', 'emergency_phone': '911', 'emergency_relationship': 'Doctor'},
    {'is_staff': 'False', 'is_active': 'True', 'is_superuser': 'False', 'username': 'john', 'set_password': 'asdf', 'first_name': 'John', 'last_name': 'Hulet', 'email': 'tcurtistest@gmail.com', 'address': 'Frosty Lane', 'city': 'Antartica', 'state': 'Utah', 'zipcode': '84604', 'phone_number': '4441115555', 'security_question': 'Am I who I say I am?', 'security_answer': 'Yes', 'emergency_contact': 'Bob', 'emergency_phone': '911', 'emergency_relationship': 'Doctor'},
    {'is_staff': 'False', 'is_active': 'True', 'is_superuser': 'False', 'username': 'landon', 'set_password': 'asdf', 'first_name': 'Landon', 'last_name': 'Meservy', 'email': 'tcurtistest@gmail.com', 'address': 'Arctic Circle Drive', 'city': 'Ancestry', 'state': 'Utah', 'zipcode': '84604', 'phone_number': '4440009999', 'security_question': 'Am I who I say I am?', 'security_answer': 'Yes', 'emergency_contact': 'Fred', 'emergency_phone': '911', 'emergency_relationship': 'Doctor'},
]:

    d = hmod.User()
    for k, v in data.items():
        setattr(d, k, v)
    d.save()

# populating data for events
for data in [
    {'name': 'Freedom Parade', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'start_date': '2015-1-1', 'end_date': '2015-1-10', 'map_file_name': 'map1.jpg', 'venue_name': 'Colonial Heritage Park', 'address1': '400 July Street', 'address2': '', 'city': 'Pittsburgh', 'state': 'PA', 'zipcode': '99999'},
    {'name': 'Patriotic Festival', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'start_date': '2015-2-2', 'end_date': '2015-2-10', 'map_file_name': 'map2.jpg', 'venue_name': 'Battlefield Park', 'address1': '501 North Street', 'address2': '', 'city': 'Boston', 'state': 'MA', 'zipcode': '44444'},
    {'name': 'Colonial Heritage Showcase', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'start_date': '2015-3-3', 'end_date': '2015-3-10', 'map_file_name': 'map3.jpg', 'venue_name': 'Flaming Island', 'address1': '325 South Street', 'address2': '', 'city': 'Pittsburgh', 'state': 'PA', 'zipcode': '99999'},
    {'name': 'Boston Tea Party', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'start_date': '2015-4-4', 'end_date': '2015-4-10', 'map_file_name': 'map4.jpg', 'venue_name': 'Mt Rushmore', 'address1': '400 June Ave', 'address2': '', 'city': 'Boston', 'state': 'MA', 'zipcode': '44444'},
    {'name': 'Battle at Fort Knox', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'start_date': '2015-5-5', 'end_date': '2015-5-10', 'map_file_name': 'map5.jpg', 'venue_name': 'Grand Canyon', 'address1': '23500 Battlefield Street', 'address2': '', 'city': 'Pittsburgh', 'state': 'PA', 'zipcode': '99999'}
]:

    d = hmod.Event()
    for k, v in data.items():
        setattr(d, k, v)
    d.save()

# populating data for area
for data in [
    {'name': 'Colonial Bakery', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'place_number': '1', 'event': hmod.Event.objects.get(id=1), 'photo': hmod.Photograph.objects.get(id=1)},
    {'name': 'Colonial Blacksmith', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'place_number': '2', 'event': hmod.Event.objects.get(id=2), 'photo': hmod.Photograph.objects.get(id=1)},
]:

    d = hmod.Area()
    for k, v in data.items():
        setattr(d, k, v)
    d.save()

# populating data for item
for data in [
    {'name': 'Mayflower Replica', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'item_value': '15000.00', 'standard_rental_price': '500.00', 'is_rentable': 'True', 'owner': hmod.User.objects.get(id=4), 'photo': 'item1.jpg'},
    {'name': 'Musket', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'item_value': '100.00', 'standard_rental_price': '12.00', 'is_rentable': 'True', 'owner': hmod.User.objects.get(id=4), 'photo': 'item1.jpg'},
    {'name': 'Chair', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'item_value': '90.00', 'standard_rental_price': '14.00', 'is_rentable': 'True', 'owner': hmod.User.objects.get(id=4), 'photo': 'item1.jpg'},
    {'name': 'Desk', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'item_value': '89.00', 'standard_rental_price': '2.00', 'is_rentable': 'True', 'owner': hmod.User.objects.get(id=4), 'photo': 'item1.jpg'},
    {'name': 'Map', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'item_value': '87.00', 'standard_rental_price': '3.00', 'is_rentable': 'True', 'owner': hmod.User.objects.get(id=4), 'photo': 'item1.jpg'},
    {'name': 'Cane', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'item_value': '67.00', 'standard_rental_price': '5.00', 'is_rentable': 'True', 'owner': hmod.User.objects.get(id=4), 'photo': 'item1.jpg'},
    {'name': 'Apron', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'item_value': '56.00', 'standard_rental_price': '4.00', 'is_rentable': 'True', 'owner': hmod.User.objects.get(id=4), 'photo': 'item1.jpg'},
    {'name': 'Belt', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'item_value': '45.00', 'standard_rental_price': '7.00', 'is_rentable': 'True', 'owner': hmod.User.objects.get(id=4), 'photo': 'item1.jpg'},
    {'name': 'Jacket', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'item_value': '34.00', 'standard_rental_price': '6.00', 'is_rentable': 'True', 'owner': hmod.User.objects.get(id=4), 'photo': 'item1.jpg'},
    {'name': 'Uniform', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'item_value': '23.00', 'standard_rental_price': '5.00', 'is_rentable': 'True', 'owner': hmod.User.objects.get(id=4), 'photo': 'item1.jpg'},
    {'name': 'Hat', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'item_value': '45.00', 'standard_rental_price': '8.00', 'is_rentable': 'True', 'owner': hmod.User.objects.get(id=4), 'photo': 'item1.jpg'},
    {'name': 'Marbles', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'item_value': '46.00', 'standard_rental_price': '7.00', 'is_rentable': 'True', 'owner': hmod.User.objects.get(id=4), 'photo': 'item1.jpg'},
    {'name': 'Boots', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'item_value': '23.00', 'standard_rental_price': '9.00', 'is_rentable': 'True', 'owner': hmod.User.objects.get(id=4), 'photo': 'item1.jpg'},
]:

    d = hmod.Item()
    for k, v in data.items():
        setattr(d, k, v)
    d.save()

# populating data for wardrobe item
for data in [
    {'name': 'Waistcoat', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'item_value': '100.00', 'standard_rental_price': '10.00', 'is_rentable': 'True', 'owner': hmod.User.objects.get(id=4), 'size': 'M', 'size_modifier': '', 'gender': 'M', 'color': '', 'pattern': '', 'start_year': '1776', 'end_year': '1780', 'note': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.'},
    {'name': 'Breeches', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'item_value': '90.00', 'standard_rental_price': '8.00', 'is_rentable': 'True', 'owner': hmod.User.objects.get(id=4), 'size': 'M', 'size_modifier': '', 'gender': 'M', 'color': '', 'pattern': '', 'start_year': '1733', 'end_year': '1799', 'note': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.'},
]:

    d = hmod.WardrobeItem()
    for k, v in data.items():
        setattr(d, k, v)
    d.save()

# populating data for rental
for data in [
    #90 days
    {'time': '2013-1-4', 'due_date': '2014-3-12', 'discount_percent': '10', 'rentee': hmod.User.objects.get(id=5)},
    {'time': '2013-1-4', 'due_date': '2014-3-2', 'discount_percent': '50', 'rentee': hmod.User.objects.get(id=5)},
    {'time': '2013-1-4', 'due_date': '2014-8-3', 'discount_percent': '50', 'rentee': hmod.User.objects.get(id=5)},
    {'time': '2013-1-4', 'due_date': '2014-8-7', 'discount_percent': '50', 'rentee': hmod.User.objects.get(id=5)},
    {'time': '2013-1-4', 'due_date': '2014-8-5', 'discount_percent': '50', 'rentee': hmod.User.objects.get(id=5)},

    # future date
    {'time': '2013-1-4', 'due_date': '2015-7-8', 'discount_percent': '50', 'rentee': hmod.User.objects.get(id=6)},
    {'time': '2013-1-4', 'due_date': '2015-7-7', 'discount_percent': '50', 'rentee': hmod.User.objects.get(id=6)},
    {'time': '2013-1-4', 'due_date': '2015-7-27', 'discount_percent': '50', 'rentee': hmod.User.objects.get(id=6)},
    {'time': '2013-1-4', 'due_date': '2015-7-24', 'discount_percent': '50', 'rentee': hmod.User.objects.get(id=6)},
    {'time': '2013-1-4', 'due_date': '2015-7-14', 'discount_percent': '50', 'rentee': hmod.User.objects.get(id=6)},

    # 30 days
    {'time': '2013-1-4', 'due_date': '2015-2-14', 'discount_percent': '50', 'rentee': hmod.User.objects.get(id=7)},
    {'time': '2013-1-4', 'due_date': '2015-2-17', 'discount_percent': '50', 'rentee': hmod.User.objects.get(id=7)},
    {'time': '2013-1-4', 'due_date': '2014-2-13', 'discount_percent': '50', 'rentee': hmod.User.objects.get(id=7)},
    {'time': '2013-1-4', 'due_date': '2014-2-2', 'discount_percent': '50', 'rentee': hmod.User.objects.get(id=7)},
    {'time': '2013-1-4', 'due_date': '2014-2-4', 'discount_percent': '50', 'rentee': hmod.User.objects.get(id=7)},

    # 60 days
    {'time': '2013-1-4', 'due_date': '2015-1-24', 'discount_percent': '50', 'rentee': hmod.User.objects.get(id=8)},
    {'time': '2013-1-4', 'due_date': '2015-1-14', 'discount_percent': '50', 'rentee': hmod.User.objects.get(id=8)},
    {'time': '2013-1-4', 'due_date': '2015-1-7', 'discount_percent': '50', 'rentee': hmod.User.objects.get(id=8)},
    {'time': '2013-1-4', 'due_date': '2015-1-3', 'discount_percent': '50', 'rentee': hmod.User.objects.get(id=8)},

    #future dare
    {'time': '2013-1-4', 'due_date': '2016-3-15', 'discount_percent': '50', 'rentee': hmod.User.objects.get(id=4)},
    {'time': '2013-1-4', 'due_date': '2016-3-18', 'discount_percent': '50', 'rentee': hmod.User.objects.get(id=4)},
    {'time': '2013-1-4', 'due_date': '2016-3-21', 'discount_percent': '50', 'rentee': hmod.User.objects.get(id=4)},
]:

    d = hmod.Rental()
    for k, v in data.items():
        setattr(d, k, v)
    d.save()

# populating data for return
for data in [
    {'time': '2015-3-12', 'fees_paid': 'True', 'fees_waived': 'False', 'agent': hmod.User.objects.get(id=6)},
    {'time': '2015-2-6', 'fees_paid': 'True', 'fees_waived': 'False', 'agent': hmod.User.objects.get(id=7)},
    {'time': '2015-2-6', 'fees_paid': 'True', 'fees_waived': 'False', 'agent': hmod.User.objects.get(id=8)},
]:

    d = hmod.Return()
    for k, v in data.items():
        setattr(d, k, v)
    d.save()

# populating data rental item
for data in [
    {'condition': 'Like New', 'late_fee': '500.00', 'due_date': '2014-12-12', 'new_damage': 'True',  'damage_fee': '10.00', 'rental': hmod.Rental.objects.get(id=1), 'item': hmod.Item.objects.get(id=1)},
    {'condition': 'Used', 'late_fee': '45.00', 'due_date': '2014-12-19', 'new_damage': 'True',  'damage_fee': '10.00', 'rental': hmod.Rental.objects.get(id=2), 'item': hmod.Item.objects.get(id=3)},
    {'condition': 'Like New', 'late_fee': '50.00', 'due_date': '2014-12-26', 'new_damage': 'True',  'damage_fee': '10.00', 'rental': hmod.Rental.objects.get(id=3), 'item': hmod.Item.objects.get(id=2)},
    {'condition': 'Like New', 'late_fee': '500.00', 'due_date': '2014-12-26', 'new_damage': 'True',  'damage_fee': '10.00', 'rental': hmod.Rental.objects.get(id=4), 'item': hmod.Item.objects.get(id=4)},
    {'condition': 'Like New', 'late_fee': '23.00', 'due_date': '2015-1-3', 'new_damage': 'True',  'damage_fee': '10.00', 'rental': hmod.Rental.objects.get(id=5), 'item': hmod.Item.objects.get(id=5)},
    {'condition': 'Used', 'late_fee': '56.00', 'due_date': '2015-1-3', 'new_damage': 'True',  'damage_fee': '10.00', 'rental': hmod.Rental.objects.get(id=6), 'item': hmod.Item.objects.get(id=7)},
    {'condition': 'Like New', 'late_fee': '576.00', 'due_date': '2015-1-3', 'new_damage': 'True',  'damage_fee': '10.00', 'rental': hmod.Rental.objects.get(id=7), 'item': hmod.Item.objects.get(id=6)},
    {'condition': 'Used', 'late_fee': '52.00', 'due_date': '2015-2-12', 'new_damage': 'True',  'damage_fee': '10.00', 'rental': hmod.Rental.objects.get(id=8), 'item': hmod.Item.objects.get(id=8)},
    {'condition': 'Like New', 'late_fee': '50.00', 'due_date': '2015-2-12', 'new_damage': 'True',  'damage_fee': '10.00', 'rental': hmod.Rental.objects.get(id=9), 'item': hmod.Item.objects.get(id=9)},
    {'condition': 'Used', 'late_fee': '500.00', 'due_date': '2015-2-19', 'new_damage': 'True',  'damage_fee': '10.00', 'rental': hmod.Rental.objects.get(id=10), 'item': hmod.Item.objects.get(id=11)},
    {'condition': 'Used', 'late_fee': '22.00', 'due_date': '2015-3-1', 'new_damage': 'True',  'damage_fee': '10.00', 'rental': hmod.Rental.objects.get(id=11), 'item': hmod.Item.objects.get(id=10)},
    {'condition': 'Like New', 'late_fee': '1.00', 'due_date': '2014-3-1', 'new_damage': 'True',  'damage_fee': '10.00', 'rental': hmod.Rental.objects.get(id=12), 'item': hmod.Item.objects.get(id=12)},
    {'condition': 'Like New', 'late_fee': '50.00', 'due_date': '2014-3-1', 'new_damage': 'True',  'damage_fee': '10.00', 'rental': hmod.Rental.objects.get(id=13), 'item': hmod.Item.objects.get(id=4)},
    {'condition': 'Like New', 'late_fee': '50.00', 'due_date': '2014-3-1', 'new_damage': 'True',  'damage_fee': '10.00', 'rental': hmod.Rental.objects.get(id=14), 'item': hmod.Item.objects.get(id=8)},
    {'condition': 'Like New', 'late_fee': '500.00', 'due_date': '2014-12-12', 'new_damage': 'True',  'damage_fee': '10.00', 'rental': hmod.Rental.objects.get(id=15), 'item': hmod.Item.objects.get(id=2)},
    {'condition': 'Used', 'late_fee': '45.00', 'due_date': '2014-12-19', 'new_damage': 'True',  'damage_fee': '10.00', 'rental': hmod.Rental.objects.get(id=16), 'item': hmod.Item.objects.get(id=3)},
    {'condition': 'Like New', 'late_fee': '50.00', 'due_date': '2014-12-26', 'new_damage': 'True',  'damage_fee': '10.00', 'rental': hmod.Rental.objects.get(id=17), 'item': hmod.Item.objects.get(id=6)},
    {'condition': 'Like New', 'late_fee': '500.00', 'due_date': '2014-12-26', 'new_damage': 'True',  'damage_fee': '10.00', 'rental': hmod.Rental.objects.get(id=18), 'item': hmod.Item.objects.get(id=5)},
    {'condition': 'Like New', 'late_fee': '23.00', 'due_date': '2015-1-3', 'new_damage': 'True',  'damage_fee': '10.00', 'rental': hmod.Rental.objects.get(id=19), 'item': hmod.Item.objects.get(id=4)},
    {'condition': 'Used', 'late_fee': '56.00', 'due_date': '2015-1-3', 'new_damage': 'True',  'damage_fee': '10.00', 'rental': hmod.Rental.objects.get(id=20), 'item': hmod.Item.objects.get(id=9)},
    {'condition': 'Like New', 'late_fee': '576.00', 'due_date': '2015-1-3', 'new_damage': 'True',  'damage_fee': '10.00', 'rental': hmod.Rental.objects.get(id=21), 'item': hmod.Item.objects.get(id=11)},
]:

    d = hmod.RentalItem()
    for k, v in data.items():
        setattr(d, k, v)
    d.save()

# populating data for product
for data in [
    {'name': 'Cannonball', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'category': 'Weapons', 'current_price': '201.15', 'product_type': 'Mass Produced', 'producer_name': 'Colonial Heritage Foundation', 'quantity_on_hand': '40', 'date_made': '2015-03-06', 'order_form_name': 'Pittsburgh', 'production_time': '2015-03-06', 'photo': 'product1.jpg'},
    {'name': 'Pistol', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'category': 'Weapons', 'current_price': '22.45', 'product_type': 'Made to Order', 'producer_name': 'Colonial Heritage Foundation', 'quantity_on_hand': '4', 'date_made': '2015-03-06', 'order_form_name': 'Pittsburgh', 'production_time': '2015-03-06', 'photo': 'product2.jpg'},
    {'name': 'Waistcoat', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'category': 'Clothing', 'current_price': '30.16', 'product_type': 'Mass Produced', 'producer_name': 'Colonial Heritage Foundation', 'quantity_on_hand': '15', 'date_made': '2015-03-06', 'order_form_name': 'Pittsburgh', 'production_time': '2015-03-06', 'photo': 'product3.jpg'},
    {'name': 'Mayflower', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'category': 'Artifacts', 'current_price': '1.25', 'product_type': 'Made to Order', 'producer_name': 'Colonial Heritage Foundation', 'quantity_on_hand': '2', 'date_made': '2015-03-06', 'order_form_name': 'Pittsburgh', 'production_time': '2015-03-06', 'photo': 'product4.jpg'},
    {'name': 'Bullets', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'category': 'Weapons', 'current_price': '999.43', 'product_type': 'Mass Produced', 'producer_name': 'Gove Allen', 'quantity_on_hand': '535', 'date_made': '2015-03-06', 'order_form_name': 'Pittsburgh', 'production_time': '2015-03-06', 'photo': 'product5.jpg'},
    {'name': 'Gun Powder', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.',  'category': 'Weapons', 'current_price': '4.75', 'product_type': 'Mass Produced', 'producer_name': 'Colonial Heritage Foundation', 'quantity_on_hand': '400', 'date_made': '2015-03-06', 'order_form_name': 'Pittsburgh', 'production_time': '2015-03-06', 'photo': 'product6.jpg'},
    {'name': 'Printing Press', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'category': 'Artifacts', 'current_price': '44.60', 'product_type': 'Mass Produced', 'producer_name': 'Colonial Heritage Foundation', 'quantity_on_hand': '400', 'date_made': '2015-03-06', 'order_form_name': 'Pittsburgh', 'production_time': '2015-03-06', 'photo': 'product7.jpg'},
    {'name': 'Pilgrim Hat', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'category': 'Clothing', 'current_price': '45.63', 'product_type': 'Mass Produced', 'producer_name': 'Colonial Heritage Foundation', 'quantity_on_hand': '400', 'date_made': '2015-03-06', 'order_form_name': 'Pittsburgh', 'production_time': '2015-03-06', 'photo': 'product8.jpg'},
    {'name': 'Wig', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'category': 'Clothing', 'current_price': '22.10', 'product_type': 'Mass Produced', 'producer_name': 'Colonial Heritage Foundation', 'quantity_on_hand': '400', 'date_made': '2015-03-06', 'order_form_name': 'Pittsburgh', 'production_time': '2015-03-06', 'photo': 'product9.jpg'},
    {'name': 'Bonnet', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'category': 'Clothing', 'current_price': '19.99', 'product_type': 'Mass Produced', 'producer_name': 'Colonial Heritage Foundation', 'quantity_on_hand': '400', 'date_made': '2015-03-06', 'order_form_name': 'Pittsburgh', 'production_time': '2015-03-06', 'photo': 'product10.jpg'},
    {'name': 'Coins', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'category': 'Collectibles', 'current_price': '199.99', 'product_type': 'Mass Produced', 'producer_name': 'Colonial Heritage Foundation', 'quantity_on_hand': '400', 'date_made': '2015-03-06', 'order_form_name': 'Pittsburgh', 'production_time': '2015-03-06', 'photo': 'product11.jpg'},
    {'name': 'Spectacles', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'category': 'Clothing', 'current_price': '87.75', 'product_type': 'Mass Produced', 'producer_name': 'Colonial Heritage Foundation', 'quantity_on_hand': '400', 'date_made': '2015-03-06', 'order_form_name': 'Pittsburgh', 'production_time': '2015-03-06', 'photo': 'product12.jpg'},
]:

    d = hmod.Product()
    for k, v in data.items():
        setattr(d, k, v)
    d.save()

# populating data for transaction
for data in [
    {'date': '2015-3-15', 'order_phone': '3333333333', 'date_packed': '2015-3-16', 'date_paid': '2015-3-15', 'date_shipped': '2015-3-16', 'customer': hmod.User.objects.get(id=1)},
    {'date': '2015-3-10', 'order_phone': '2223332222', 'date_packed': '2015-3-11', 'date_paid': '2015-3-10', 'date_shipped': '2015-3-11', 'customer': hmod.User.objects.get(id=1)},
]:

    d = hmod.Transaction()
    for k, v in data.items():
        setattr(d, k, v)
    d.save()


# populating data for order detail
for data in [
    {'quantity': '5', 'price': '10.00', 'order_file': 'akdoehwo0', 'transaction': hmod.Transaction.objects.get(id=1), 'product': hmod.Product.objects.get(id=1)},
    {'quantity': '1', 'price': '1000.00', 'order_file': 'adfgr420', 'transaction': hmod.Transaction.objects.get(id=1), 'product': hmod.Product.objects.get(id=1)},
]:

    d = hmod.OrderDetail()
    for k, v in data.items():
        setattr(d, k, v)
    d.save()

# populating data for shopping cart
for data in [
    {'sale_date': '2015-3-15', 'shipping_handling': '4.99', 'tax': '2.98', 'total_amount': '18.97', 'shipping_tracking_number': '209341509', 'customer': hmod.User.objects.get(id=1)},
    {'sale_date': '2015-3-15', 'shipping_handling': '10.99', 'tax': '17.98', 'total_amount': '1096.44', 'shipping_tracking_number': '21461347509', 'customer': hmod.User.objects.get(id=1)},
]:

    d = hmod.ShoppingCart()
    for k, v in data.items():
        setattr(d, k, v)
    d.save()

# populating data for cart item
for data in [
    {'quantity': '10', 'sold_price': '18.97', 'product': hmod.Product.objects.get(id=1), 'shopping_cart': hmod.ShoppingCart.objects.get(id=1)},
    {'quantity': '1', 'sold_price': '1094.97', 'product': hmod.Product.objects.get(id=1), 'shopping_cart': hmod.ShoppingCart.objects.get(id=1)},
]:

    d = hmod.CartItem()
    for k, v in data.items():
        setattr(d, k, v)
    d.save()

# populating data for sale item
for data in [
    {'name': 'Teapot', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'low_price': '10', 'high_price': '19', 'artisan_name': hmod.User.objects.get(id=1), 'area': hmod.Area.objects.get(id=1)},
    {'name': 'Horseshoe', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'low_price': '25', 'high_price': '53', 'artisan_name': hmod.User.objects.get(id=1), 'area': hmod.Area.objects.get(id=1)},
]:

    d = hmod.SaleItem()
    for k, v in data.items():
        setattr(d, k, v)
    d.save()