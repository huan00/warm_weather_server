from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = (
                  'id',
                  'username', 
                  'password',
                  'email', 
                  'first_name', 
                  'last_name', 
                  'address', 
                  'city', 
                  'state', 
                  'zip_code'
                  )
    
    def create(self, validated_data):
        for data in validated_data:
            if data != 'password':
                validated_data[data] = validated_data[data].lower()
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)

class UserUpdateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)
    email = serializers.CharField(read_only=True)

    
    class Meta:
        model = User
        fields = (
                    'id', 
                    'username',
                    'email',
                    'first_name', 
                    'last_name', 
                    'address', 
                    'city', 
                    'state', 
                    'zip_code'
                  )
        

