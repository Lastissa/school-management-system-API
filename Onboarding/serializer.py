from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db import IntegrityError, transaction
import logging

from Utiltiy.abstract import user_key_error

logger = logging.getLogger(__name__)

class StudentApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['role', 'email', 'password', 'is_active']
        extra_kwargs = {
            'role': {'read_only': True},
            'is_active': {'read_only': True},
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        try:
            with transaction.atomic():
                user = get_user_model().objects.create_interested_applicant(**validated_data)
                return user
        except IntegrityError as e:
            raise serializers.ValidationError(user_key_error(e))
        except Exception as e:
            raise serializers.ValidationError(f"error :{e}")
        
        

class CreateMngtAccSerializer(StudentApplicationSerializer):
    """
    Serialize entry for creating management account
    This allow custom user_key but if that user_key is taken, return 'it cannot be used'
    If no user_key is provided, default to using the random one used for others
    """
    class Meta:
        model = get_user_model()
        fields = ['role', 'email', 'password', 'is_active', 'user_key']
        extra_kwargs = {
            'role': {'read_only': True},
            'is_active': {'read_only': True},
            'password': {'write_only': True},
            'user_key': {'allow_blank': True}
        }

    
    def create(self, validated_data):
        try:
            with transaction.atomic():
                user = get_user_model().objects.create_mngt_accout(**validated_data)
                return user
        except IntegrityError as e:
            raise serializers.ValidationError(user_key_error(e))
        except Exception as e:
            raise serializers.ValidationError(f"error :{e}")
    

    
    