"""
THIS FILE SERVES AS ABSTRACTION FOR OTHER FILES THAT I DO NOT WANT SOME VISIBLE CONTENT THERRE
"""

import hmac
from django.conf import settings
import logging

logger= logging.getLogger(__name__)

def compare_sy_secret(incoming, email = None, password = None):
    """COMPARE THE INCOMING WITH THE ACTUAL SY KEY
    """
    if not incoming or not email or not password:
        logger.warning(msg=f"Incoming threath discovered with the details: 'email: {email}, password= {password}'")
        return False
    key = settings.SY_SECRET
    if not key: 
        logger.warning(msg=f"Incoming treath discovered with the details: 'email: {email}, password= {password}'")
        return False
    if not hmac.compare_digest(key,incoming):
        logger.warning(msg=f"AMDIN ACCOUNT CREATION sy_secret compare failed  for the the details: 'email: {email}, password= {password}'")
        return False
    return True


def optimization():
    """
    During dev, to check the amount of database callup i am using
    For better test, call
    """
    from django.db import connection
    total_sql = 0
    total_dur = 0
    for i in connection.queries:
        if float(i['time']) > 0:
            print(f"sql: {i['sql']}, time: {i['time']}")
            total_dur += float(i['time'])
            total_sql += 1
            
    print(f"Total sql is {total_sql} and total duration is {total_dur}")
        
        
        

    