from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path('login/', views.Login.as_view(), name = 'user_key_login'),
    path('refresh_token/', views.RefreshToken.as_view(), name="refresh_token"),
    path('verify_token/', TokenVerifyView.as_view(), name = 'token_verify') #   Verify if token is still valid, for frontend useage maybe to check if user is still valid and remind them to do something
]
