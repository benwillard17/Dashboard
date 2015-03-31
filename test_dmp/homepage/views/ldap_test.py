from ldap3 import Server, Connection, AUTH_SIMPLE, STRATEGY_SYNC, STRATEGY_ASYNC_THREADED, SEARCH_SCOPE_WHOLE_SUBTREE, GET_ALL_INFO
# import homepage.models as hmod

domain = 'CHERITAGE\\'
username = 'ben'
pw = 'UCon2014'

try:
    s = Server('128.187.61.39', port=8889, get_info=GET_ALL_INFO)
    c = Connection(s, auto_bind=True, client_strategy = STRATEGY_SYNC,
                    user=domain+username,
                    password=pw, authentication=AUTH_SIMPLE
                    )
    print(c)

    u.created = hmod.User.objects.get_or_create(user=username)
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



#check if that is the right if statement
if c != None:
    print(c)
else:
    print("fasdl;")
    # now that we know it is a valid user, get the user account from Dango
    u.created = hmod.User.objects.get_or_create(username=username)
    u.first_name = s.first_name
    u.last_name = s.last_name
    u.email = s.email
    u.set_password(pw)
    u.save()

    print(s.first_name)
    print(s.last_name)
    print(s.username)
    print(s.password)
    print(s.pw)

    #now log the user in
    # u2 = authenticate(netid, pw0)
    # login(request, u2)
