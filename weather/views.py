from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import generics, permissions
from .serializer import WeatherSerializer
from .models import Weather
# Create your views here.


# class CurrentWeather(generics.CreateAPIView):
#     permission_classes = [permissions.AllowAny]


@csrf_exempt
@api_view(['GET', 'POST'])
def weather_list(request):
    # before creating weather we need to create survey

    if request.method == 'POST':
        data = request.data
        date = request.data['date']
        zip_code = request.data['zip_code']
        location = request.data['location']
        date_exist = Weather.objects.filter(date=date)
        print(date_exist)
        if date_exist:
            return HttpResponse('exist')
        else:
            return HttpResponse('don\'t exist')
