from django.urls import path, include

from .views import RegisterUser, LoginView, UpdateView, DeleteView
from rest_framework import viewsets
from . import views

urlpatterns = [
    path('register', RegisterUser.as_view(), name='create_user'),
    path('login', LoginView.as_view(), name='login_user'),
    path('update/<int:pk>', UpdateView.as_view(), name='update_user'),
    path('delete/<int:pk>', DeleteView.as_view(), name='delete_user')
]