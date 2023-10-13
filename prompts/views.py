from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from .serializers import PromptsSerializer
from .models import Prompts
from user.models import User


# Create your views here.

class PromptsView(generics.CreateAPIView):
  # permission_classes = [permissions.AllowAny]
  authentication_classes = [TokenAuthentication]
  permission_classes=[permissions.IsAuthenticated]

  serializer_class = PromptsSerializer

  def post(self, request):
    # try:
    user = User.objects.get(pk=Token.objects.get(key=request.auth).user_id).pk
    print( user)

    data = {
      'gender': request.data['gender'],
      'sensitivity_to_cold': request.data['sensitivity_to_cold'],
      'User': user
    }
    
    print(data)
    prompts_serializer = self.serializer_class(data=data)

    if prompts_serializer.is_valid(raise_exception=True):
      prompts = self.create(prompts_serializer)
      return Response(prompts.data)
    

  def put(self, request):
    
    user = User.objects.get(pk=Token.objects.get(key=request.auth).user_id).pk

    exist_prompt = Prompts.objects.get(User_id=user)

    prompt_serializer = PromptsSerializer(exist_prompt).data
    for el in request.data:
      prompt_serializer[el] = request.data[el]

    print(prompt_serializer)
    
    prompt_serializer = PromptsSerializer(exist_prompt, data=prompt_serializer)

    prompt_serializer.is_valid(raise_exception=True)
    prompt_serializer.save()

    return Response(prompt_serializer.data)