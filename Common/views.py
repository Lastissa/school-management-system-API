
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializer import LoginSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView 


Schema=get_user_model()

class Login(TokenObtainPairView):
    """
    Generate a signed token and refresh for valid user
    This endpoint expect a user_key login but for new user with no user_key, they will get redirected to another class that will handle email login
    but email login will mainly be for something less important.
    """
    
    serializer_class = LoginSerializer


    
class RefreshToken(TokenRefreshView):
    """### Refresh Token
    I purposedly wrapped it like this for easier code remembrance
    Only collect the resfresh key and return a new access key
    """
    pass