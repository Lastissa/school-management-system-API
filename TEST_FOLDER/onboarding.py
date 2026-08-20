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
    
    
interest_stundet_account_creation()

