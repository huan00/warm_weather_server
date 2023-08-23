from django.shortcuts import render
from rest_framework.response import Response
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import generics, permissions,status
from .serializers import WeatherSerializer
from .models import Weather
# Create your views here.


class CurrentWeather(generics.CreateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]
    serializer_class = WeatherSerializer


    def post(self, request):
        weather_serializer = self.serializer_class(data=request.data)

        if weather_serializer.is_valid(raise_exception=True):
            weather_exist = Weather.objects.filter(
                                                weather_date=weather_serializer.data['weather_date'],
                                                zip_code=weather_serializer.data['zip_code'], 
                                                location=weather_serializer.data['location']
                                                )
            if not weather_exist:
                weather = self.create(weather_serializer)
                return Response(weather.data, status=status.HTTP_200_OK)
            else:
                
                weather = self.serializer_class(weather_exist, many=True)

                return Response(weather.data, status=status.HTTP_200_OK)



