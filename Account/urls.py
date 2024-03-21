from django.urls import path 
from .views import RegistrationApi,LoginApi,ProfileListCreateAPIView, ProfileRetrieveUpdateDestroyAPIView,CustomUserListCreateAPIView, CustomUserRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('register',RegistrationApi.as_view()),
    path('login',LoginApi.as_view()), 
    path('profiles/', ProfileListCreateAPIView.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', ProfileRetrieveUpdateDestroyAPIView.as_view(), name='profile-detail'),
    path('users/', CustomUserListCreateAPIView.as_view(), name='customuser-list-create'),
    path('users/<int:pk>/', CustomUserRetrieveUpdateDestroyAPIView.as_view(), name='customuser-detail'),
]
