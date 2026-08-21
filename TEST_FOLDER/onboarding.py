"""
HANDLE TEST RELATED TO ONBOARIDNG DJANGO APP
"""

import requests
import json

home = "http://localhost:8000/"


def interest_stundet_account_creation():
    """TEST THE INTERESTED STUDENT ACCOUNT CREATION ENDPOINT"""
    url = home + 'api/onboarding/student/'
    data = {
        'email': 'test@interestedstudent.com',
        'password': 'Adddddd'
    }
    res = requests.post(url=url, json=data)
    print(json.loads(res.text))
    
    
def management_account_creation():
    """TEST THE ENDPOINT IN CHARGE OF SCHOOL MANAGEMENT ACCOUNT CREATION, NEEED ADMIN OR MANAGEMENT TO BE LOGIN
    AUTHENTICATION REQ, CALL LOGIN ENDPOINT TO GETAUTHENTICATION FIRST
    """
    # #############################################################################################
    # #   Get the creds, Print to terminal, cpopyt copy both the refresh and access
    # from common import login
    # credentials = login(user_key = 'AD2206', password = "Allahu123")
    # if "error".upper() in "".join(credentials.keys()).upper(): 
    #     print("Cant proceed with managemnet account creation as logging in already give error")
    #     return 0
    # #############################################################################################
    refresh = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc4NzM4MDkwOSwiaWF0IjoxNzg3MzM3NzA5LCJqdGkiOiI3ZjgyNzFhMGE3NzY0NzBlODk5ZjI1ZDMwNzYzZTU5NyIsInVzZXJfaWQiOiIzIiwiZW1haWwiOiJMQVNUSVNTQTFAR01BSUwuQ09NIiwicm9sZSI6IkFETUlOIiwidXNlcl9rZXkiOiJBRDIyMDYifQ.cZk7MeQkFinkYiPvRfk_mLj4fWeLvHYi6nOjTMrABPY"
    access = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzg3MzM4NzY0LCJpYXQiOjE3ODczMzg0NjQsImp0aSI6IjY1MzczMWI3ZDBjNjRkMmI4ZWNmMjA3NTQ5Yzc2MTUzIiwidXNlcl9pZCI6IjMiLCJlbWFpbCI6IkxBU1RJU1NBMUBHTUFJTC5DT00iLCJyb2xlIjoiQURNSU4iLCJ1c2VyX2tleSI6IkFEMjIwNiJ9.aVFGUR3f_-zPeBS6-0eQhCTKYG-p10xgLvrHFX5YTnM"
    ##############################################################################################
    # # INCASE TOKEN EXPIRE, USE THIS LINK TO GET NEW ONE
    # from common import refresh_token
    # access = refresh_token(refresh)
    # ##############################################################################################
    url = home + 'api/onboarding/mngt/'
    data = {
        'email': 'test@dudent.com',
        'password': 'Adddddd',
        'user_key': "ma02020"   #   Optional
    }
    headers = {
        'Authorization': f"Bearer {access}" 
    }
    res = requests.post(url=url, json=data, headers = headers)
    print(json.loads(res.text))






# interest_stundet_account_creation()
management_account_creation()

