"""
Common DjangoApp Test and ALSO THE LOGIN AND REFRESH 
"""

import json, requests

home = "http://localhost:8000/"
def login(user_key = '', password = ''):
    """LOOK UP A VALID USER AND RETURN REFRESH KEY AND ACCESS KEY"""
    data = {
        'user_key': user_key,
        'password': password
    }
    url = home + "api/account/login/"
    res = requests.post(url = url, json= data)
    print(json.loads(res.text))
    return json.loads(res.text)
    
    
    
    
    
    
    
def refresh_token(refresh= ''):
    "TO COLLECT A NEW ACCESS TOKEN "
    url = home + "api/account/refresh_token/"
    res = requests.post(url = url, json= {'refresh': refresh})
    print(json.loads(res.text))
    return json.loads(res.text)
    
# login()
refresh_token()

