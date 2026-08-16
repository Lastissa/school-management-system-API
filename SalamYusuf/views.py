from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CreateSYAccSerializer
from django.contrib.auth import get_user_model
from Utiltiy.abstract import compare_sy_secret

Schema = get_user_model()

class CreateSYAcc(APIView):
    serializer_class = CreateSYAccSerializer
    
    def get(self, request, email = None, password = None, sy_secret_incoming = None):
        if not compare_sy_secret(email =email, password =password, incoming=sy_secret_incoming): return JsonResponse({'message': 'ERROR; missing params, your action have been logged'})
        data = {
            'email': email,
            'password':password,
        }
        istance = CreateSYAccSerializer(Schema, data = data)
        if istance.is_valid():
            istance.save()
            return Response(istance.data, status = 200)
        return Response(istance.errors, status = 400)