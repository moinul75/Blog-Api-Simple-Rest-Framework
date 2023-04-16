from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken



#make a Registration and Login Serializer form Serializers 
class RegistrationSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()
    
    
    #validate 
    def validate(self, data):
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError("Username is Already Taken...")
        elif User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError("Email is Already Taken..Please Choose Another One")
        elif data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Password Didn't Matched..")
        return data
    
    def create(self, validated_data):
        user = User.objects.create(
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email'],
            username = validated_data['username'].lower()
        )
        user.set_password(validated_data['password'])
        user.save()
        return validated_data
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()
    
    def get_token(self,data):
        user = authenticate(username=data['username'],password=data['password'])
        
        if not user:
            return {'message':'Invalid User','data':{}}
        
        refresh = RefreshToken.for_user(user)
        return {'message':'successfully get the token','data':{  'refresh': str(refresh),
        'access': str(refresh.access_token),
        }}
        
    
