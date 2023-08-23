from django.urls import path, include
from .views import CurrentWeather
from . import views

urlpatterns = [
    path('create', CurrentWeather.as_view(), name='create_weather')
]
