from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils import timezone

Schema = get_user_model()

class LoginSerializer(TokenObtainPairSerializer):
    """Login serializer using user_key for authentication"""
    
    user_key = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, attrs):
        user = Schema.objects.filter(user_key__iexact=attrs['user_key'].strip()).first()
        
        if not user:
            raise serializers.ValidationError("No Account Found With This User or Incorrect password")
        if not user.check_password(attrs['password']):
            raise serializers.ValidationError("No Account Found With This User or Incorrect password")
        if not user.is_active:
            raise serializers.ValidationError("Account is deactivated")
        
        # Update last login
        user.last_login = timezone.now()
        user.save(update_fields=['last_login'])
        
        # Generate tokens using parent class
        data = super().validate(attrs)
        
        # Add custom data to response
        data.update({
            'email': user.email,
            'role': user.role,
            'is_active': user.is_active,
        })
        
        return data
    
    #Overide the default get_token behaviour for data represnetation to the user
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # Add custom claims to token
        token['email'] = user.email
        token['role'] = user.role
        token['user_key'] = user.user_key
        
        return token
    
    
