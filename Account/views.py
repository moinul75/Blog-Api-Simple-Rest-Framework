from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from .serializers import RegistrationSerializer ,LoginSerializer,ProfileSerializer ,CustomUserSerializer
from .models import CustomUser,Profile 
from rest_framework import generics,permissions,pagination,filters 
from rest_framework.permissions import IsAuthenticated 
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.
class RegistrationApi(APIView):
    def post(self,request):
        data = request.data 
        serializer = RegistrationSerializer(data=data)
        try:
            if not serializer.is_valid():
                return Response(
                    {
                        'data':serializer.errors,
                        'message':"Something Is Went Wrong..."
                    },status=status.HTTP_400_BAD_REQUEST
                )
            serializer.save()
            return Response(
                {
                    'data':serializer.data,
                    'message':"Successfully Register The User..."
                },status=status.HTTP_201_CREATED
            )
        except Exception as e:
            print(e)
            return Response(
                {
                    'data':serializer.errors,
                    'message':'Something went wrong...'
                },status=status.HTTP_400_BAD_REQUEST
            )
    
class LoginApi(APIView):
    def post(self,request):
        data =request.data 
        serializer = LoginSerializer(data=data)
        try:
            if not serializer.is_valid():
                return Response(
                    {
                        'data':serializer.errors,
                        'message':'Something Went Wrong...'
                    }
                )
            response = serializer.get_token(serializer.data)
            return Response(response,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(
                {
                    'data':serializer.errors,
                    'message':'Something is went Wrong...'
                },status=status.HTTP_400_BAD_REQUEST
            )
            
class CustomUserListCreateAPIView(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class CustomUserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]
       
class ProfileListCreateAPIView(ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)

class ProfileRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)
    
            
