from .classes.Authorization import Authorization

print("Console life.")
token = open("./token.txt", "r")

if token is None:
    auth = Authorization()
    auth.sign()
else:
    print("Hi user, we need to check your token")