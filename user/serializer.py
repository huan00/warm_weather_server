from rest_framework import serializers
from .models import User


class UserSerializer(serializers.Serializer):
    
    class Meta:
        model = User
        fields = ('id', 
                  'username', 
                  'email', 
                  'first_name', 
                  'last_name', 
                  'address', 
                  'city', 
                  'state', 
                  'zip_code')