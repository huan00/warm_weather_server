from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView

# Create your views here.

class SurveyView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    