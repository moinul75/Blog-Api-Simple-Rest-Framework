from django.urls import path 
from .views import RegistrationApi,LoginApi

urlpatterns = [
    path('register',RegistrationApi.as_view()),
    path('login',LoginApi.as_view()),
]
