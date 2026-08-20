from rest_framework import serializers
from django.db import transaction
from django.contrib.auth import get_user_model
import logging

logger= logging.getLogger(__name__)
Schema = get_user_model()
class CreateSYAccSerializer(serializers.ModelSerializer):
    """### TASK: CREATE ADMIN ACCOUNTS
    Raise Common error on purpose to avoid leaking internal information
    """
    email = serializers.EmailField()
    password = serializers.CharField(min_length = 3, write_only = True)
    
    class Meta:
        model = Schema
        fields = '__all__'
        extra_kwargs = {
            'role': {'read_only': True},
            'user_key': {'read_only': True},
            'is_active': {'read_only': True},
            'email_verified':  {'read_only': True},
            'date_created':  {'read_only': True},
            'last_login':  {'read_only': True},
            'is_staff': {'read_only': True},
            'is_mngt': {'read_only': True},
        }
        
    
    def create(self, validated_data):
        try:
            with transaction.atomic():
                user = Schema.objects.create_admin(**validated_data)
                return user
        except Exception as e:
            logger.error(msg=f"Error experience while creating account for the user {validated_data.get('email')} with exception: '{e}'")
            raise serializers.ValidationError("Error while creating account, refer to logs or contact support.", code="database_level_error")
    

    
    