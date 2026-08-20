from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CreateSYAccSerializer
from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.db import reset_queries
from Utiltiy.abstract import compare_sy_secret, optimization


import logging
logger = logging.getLogger(__name__)
Schema = get_user_model()





class CreateSYAcc(APIView):    
    serializer_class = CreateSYAccSerializer
    def get(self, request, email = None, password = None, sy_secret_incoming = None):
        reset_queries()
        key= f'admin-create:{email}'.upper()
        limit=cache.get(key)    #   Increase exponentially 1,2,4,8,etc
        logger.info(msg=f"Current rate limited statuf of email '{email}' is {limit}")
        if limit:
            if limit >=60: new_lim = 60
            else:new_lim= limit*2
            cache.set(key, new_lim, timeout=new_lim)
            return JsonResponse({'message': f'try again in the next {new_lim} seconds, try before time end increase ban time'})
        cache.set(key, 1, timeout=1)        #Made this indpendedt so below code after theif not can use it
        if not compare_sy_secret(email =email, password =password, incoming=sy_secret_incoming):
            return JsonResponse({'message': 'ERROR; missing params, your action have been Noted, avoid spam as you will be restricted',})
        data = {
            'email': email,
            'password':password,
        }
        istance = CreateSYAccSerializer(data = data)
        if istance.is_valid():
            istance.save()
            optimization()
            return Response(istance.data, status = 200)
        return Response(istance.errors, status = 400)
    