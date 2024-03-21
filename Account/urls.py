from django.urls import path 
from .views import RegistrationApi,LoginApi,ProfileListCreateAPIView, ProfileRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('register',RegistrationApi.as_view()),
    path('login',LoginApi.as_view()), 
    path('profiles/', ProfileListCreateAPIView.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', ProfileRetrieveUpdateDestroyAPIView.as_view(), name='profile-detail'),
]
