

#for the email
token = default_token_generator.make_token(user),
#checker
#underneath the is form valid
if user is not None and default_token_generator.check_token(user, token):