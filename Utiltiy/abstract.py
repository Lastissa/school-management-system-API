"""
##############################################################################################

THIS FILE SERVES AS ABSTRACTION FOR OTHER FILES THAT I DO NOT WANT SOME VISIBLE CONTENT THERRE

##############################################################################################

"""

import hmac
from django.conf import settings
from django.core.cache import cache
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
    

##############################################
# KNOWING THE IP COMING FROM THE REQUEST
# NB: This can be swapped with anything sice its only used by the rate limtiing itselg
# I CAN DECIDE TO CHANGE FROM HERE WETHER TO NOT USE IP BAN AND USE SOMETHING ELSE
#############################################
    
def _client_ip(request):
    """
    Look for the client IP adress to ban.
    Now some issue of render load balancer so give REMOTE_ADDR to be only a fallback and HTTP_X_FORWARED is the main one
    difference? X.. append all ip since the request was mad down to the last load balancer ip
    issue, attacker can spoof this but i no get choice since render uses a load balancer
    """
    forwarded = request.META.get('HTTP_X_FORWARDED_FOR')
    if forwarded:
        return forwarded.split(',')[0].strip()  #   Get the very first IP
    return request.META.get('REMOTE_ADDR', 'unknown')


##############################################
# RATE LIMTIING
# LOOK IN THE CACHE FOR THE KEY
#############################################
def _rate_limited(key_prefix, request, limit=5, window_seconds=60):
    """
    Used the ip addr from _client_ip to enforce rat limit, the only issue; this might no work
    because if the attacker append data to their x-for.. data then they will bypass it
    but incase x=for.. is nto found, default to just use the immediate rrquest sender(remote_a...)
    """
    key = f'{key_prefix}:{_client_ip(request)}'
    count = cache.get(key, 0)
    if count >= limit:
        #reset the counter
        cache.set(key, count + 1, timeout=window_seconds)
        return True
    cache.set(key, count + 1, timeout=window_seconds)
    return False


def user_key_error(exception:Exception) -> str:
    """
    ### Look into the exception message looking for user_key constraint error
    ### if it see it there, then automatically, it can only happen if multiple user with the same role are trying to create account at the exact same time
    ### This avoid leving the error unclear as it inform them of heavyconcurrency
    ## NB: USE THIS ONLY UNDER A UNIQUE CONSTRAINT ERROR
    """
    return "Too much traffic, please try again now. You cannot see this error 5 consequentive times" if "user_key" in str(exception) else "Email already in use"
    
        
        
        

    