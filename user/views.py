from django.shortcuts import render
from .models import User
from survey.models import Survey
from survey.serializers import UserSurveySerializer
from rest_framework.authtoken.models import Token
from rest_framework import viewsets, permissions, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserUpdateSerializer, UserSurveyDetailSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
import bcrypt
import openai

import os

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']

# Create your views here.


class RegisterUser(CreateAPIView):
    permissions_classes = [permissions.AllowAny]
    serializer_class = UserRegisterSerializer
    
    # register view logic
    def post(self, request):
        # create a serializer of the input data
        serializer = self.serializer_class(data=request.data)
        # if data are valid create user, else raise error
        if serializer.is_valid():
            print(serializer)
            # if not isinstance(int(serializer.data['zip_code']), int):
            #     raise ValueError('Zip code is invalid')

            # call create function to create user
            self.create(serializer)    
            # get user instance from database for token creations.
            user = User.objects.get(username=serializer.data['username'].lower())
            token = Token.objects.create(user=user)

            # return reponse
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            print(serializer.data)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(ObtainAuthToken):
    serializer_class = UserLoginSerializer
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

class UpdateView(ObtainAuthToken):
    # permissions_classes = [permissions.AllowAny]
    authentication_classes = [TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]


    def put(self, request, pk=None):
        token = request.auth
        user_id = Token.objects.get(key=token).user_id

        # check if token user match pk user
        #return error if don't match
        if pk != user_id:
           return Response({'error': 'user input conflict'}, status=status.HTTP_409_CONFLICT)

        # get user from database
        user = User.objects.get(pk=pk)
        # get data info from database
        user_serializer = UserUpdateSerializer(user).data

        # update user data from request data
        for data in request.data:
            if data == 'zip_code':
                if not isinstance(int(request.data[data]), int):
                    raise ValueError('zip code unacceptable, please check!')
            user_serializer[data] = request.data[data].lower()
        
        # serializer updated data
        user_serializer = UserUpdateSerializer(user, data=user_serializer)
        # if data doesn't pass serializer raise error, else Save it.
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()

        # return updated user to client.
        return Response(user_serializer.data, status=status.HTTP_202_ACCEPTED)

class DeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def delete(self, request, pk=None):
        user_id = Token.objects.get(key=request.auth).user_id

        # make sure user_id and pk are the same before delete
        if pk != user_id:
            return Response({'error': 'user input conflict'}, status=status.HTTP_409_CONFLICT)
        
        user = User.objects.get(pk=pk)
        user.delete()

        return Response({"message": "user deleted"}, status=status.HTTP_202_ACCEPTED)

class GetUserView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]

    def get(self, request, pk=None):
        user = User.objects.get(pk=pk)
        user_serializer = UserSurveyDetailSerializer(user)

        return Response(user_serializer.data)
    

    
# analyze survey question answer and associated weather to determine, if user will be cold today.
class GiveFeedBack(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, pk=None):
        surveys = Survey.objects.filter(user=pk)
        survey_serializer = UserSurveySerializer(surveys, many=True)
        
        # should i use openai or no.
        # question should have tempeature and realfeel.

        print(survey_serializer.data)
        return Response(survey_serializer.data)