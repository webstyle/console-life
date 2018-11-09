from .classes.Authorization import Authorization
from .classes.token_validation import token_validation as Token

print("Console life.")
token = open("./token.txt", "r")

if token is None:
    auth = Authorization()
    auth.sign()
else:
    token_validation = Token(token)
    if token_validation.is_valid:
        print("Hello!!!")
    else:
        print("logout")
