from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db import IntegrityError, transaction


class StudentApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['role', 'email', 'password', 'is_active']
        extra_kwargs = {
            'role': {'read_only': True},
            'is_active': {'read_only': True},
            'password': {'write_only': True}
        }
        
    def validate(self, attrs):
        super().validate(attrs) #   Call to allow defalt serializer run first
        attrs['email'] = attrs['email'].upper()
        print(attrs)
        return attrs
    
    def create(self, validated_data):
        try:
            with transaction.atomic():
                user = get_user_model().objects.create_interested_applicant(**validated_data)
                return user
        except IntegrityError:
            raise serializers.ValidationError("Email already taken")
        except Exception as e:
            raise serializers.ValidationError(f"error :{e}")