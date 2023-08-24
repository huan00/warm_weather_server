from django.urls import path, include

from .views import RegisterUser, LoginView, UpdateView, DeleteView, GetUserView, GiveFeedBack
from rest_framework import viewsets
from . import views

urlpatterns = [
    path('register', RegisterUser.as_view(), name='create_user'),
    path('login', LoginView.as_view(), name='login_user'),
    path('update/<int:pk>', UpdateView.as_view(), name='update_user'),
    path('delete/<int:pk>', DeleteView.as_view(), name='delete_user'),
    path('get_user/<int:pk>', GetUserView.as_view(), name='get_user' ),
    path('feedback/<int:pk>', GiveFeedBack.as_view(), name='feedback')
]
