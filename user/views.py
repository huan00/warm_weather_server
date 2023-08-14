from django.shortcuts import render
from .models import User
from rest_framework.authtoken.models import Token
from rest_framework import viewsets, permissions, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework import authentication
from django.contrib.auth.hashers import make_password

from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .serializers import UserSerializer 
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
import bcrypt
# Create your views here.


class RegisterUser(CreateAPIView):
    # queryset = User.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
    
    # register view logic
    def post(self, request):
        # create a serializer of the input data
        serializer = self.serializer_class(data=request.data)
        # if data are valid create user, else raise error
        if serializer.is_valid(raise_exception=True):
            if not isinstance(int(serializer.data['zip_code']), int):
                raise ValueError('Zip code is invalid')

            # call create function to create user
            self.create(serializer)    
            # get user instance from database for token creations.
            user = User.objects.get(username=serializer.data['username'].lower())
            token = Token.objects.create(user=user)

            # return reponse
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



        

class LoginView(ObtainAuthToken):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        # authenticate user with username and password
        password = request.data['password']
        username = request.data['username']
        user = authenticate(username=username, password=password)
        
        # if no user found return with error
        if not user:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

        # pull user data for requested user
        userData = self.serializer_class(User.objects.get(username=user))
        # create token for user
        token = Token.objects.get_or_create(user=user)

        # create reponse data with user and token
        response_data = {'token': token[0].key, 'data': userData.data}
        
        if token and userData:
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'unable to retrive user'}, status=status.HTTP_404_NOT_FOUND)


