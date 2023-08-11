from django.shortcuts import render
from .models import User
from rest_framework.authtoken.models import Token
from rest_framework import viewsets, permissions, status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .serializers import UserSerializer
# Create your views here.


class RegisterUser(CreateAPIView):
    permissions_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)
            return Response({'token': token.key})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)