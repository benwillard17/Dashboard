#is this a valid user?
netid = 'ben17'
pw = 'password1'
from ldap3 import Server, Connection, AUTH_SIMPLE, STRATEGY_SYNC, GET_ALL_INFO
s = Server('byuldap.byu.edu', port=389, get_info=GET_ALL_INFO)
c = Connection(s, client_strategy = STRATEGY_SYNC,
				user='cn=%s, ou=people, o=ces' % netid, 
				password=pw, authentication=AUTH_SIMPLE
				)
print(c)
#check if that is the right if statement
# if c != None:
# 	#now that we know it is a valid user, get the user account from Dango
# 	u, created = hmod.User.objects.get_or_create(username=netid)
# 	u.first_name = c.
# 	u.last_name = c.
# 	u.email = c.
# 	u.set_password(pw)
# 	u.save()

# 	#now log the user in
# 	u2 = authenticate(netid, pw0)
# 	login(request, u2)

# else:
# #run the regular login code that you already have
