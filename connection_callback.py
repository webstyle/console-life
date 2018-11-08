import jwt

def connection_callback(ch, method, properties, body):
    token = jwt.encode({'id': 'someUserId', 'name': str(body)}, 'secret', algorithm='HS256')
    print("name  :"+ str(body))
    print(token)
    return token