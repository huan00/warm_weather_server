from django.urls import path, include

from .views import RegisterUser, LoginView
from . import views

urlpatterns = [
    path('register', RegisterUser.as_view(), name='create_user'),
    path('login', LoginView.as_view(), name='login_user')
    # path('login', views.loginView, name='login')
]
