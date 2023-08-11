from django.urls import path, include

from . import views

urlpatterns = [
    path('create/', views.weather_list, name='create_weather')
]
