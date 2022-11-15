from rest_framework import generics, permissions
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import User_Data,DeviceDetails
from rest_framework.validators import ValidationError

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Data
        fields = '__all__'

    # def validate(self,attrs):
    #     email_exists = User_Data.objects.filter(email = attrs['email']).exists()
    #     if email_exists:
    #         raise ValidationError('Email has already been used')

    #     return super().validate(attrs)

class DeviceDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceDetails
        fields = '__all__'


# Register Serializer
class AddUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        
# User Serializer
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'email','password')
