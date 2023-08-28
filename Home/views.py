from django.shortcuts import render
from .models import Blog
from .serializers import blogSerializer
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from django.core.paginator import Paginator
# Crud of Blog 
class BlogApi(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def post(self,request):
        data = request.data 
        data['user'] = request.user.id
        serializer = blogSerializer(data=data)
        try:
            if not serializer.is_valid():
                return Response(
                    {
                        'data':serializer.errors,
                        'message':'Something is went Wrong'
                    },status=status.HTTP_400_BAD_REQUEST
                )
            else:
                serializer.save()
                return Response(
                    {
                        'data':serializer.data,
                        'message':'Successfully Created Posts'
                    },status=status.HTTP_201_CREATED
                )
        except Exception as e: 
            print(e)
            return Response(
                {
                    'data':serializer.errors,
                    'message':'Something is went Wrong..'
                },status=status.HTTP_400_BAD_REQUEST
            )
    def get(self,request):
        try:
            blog = Blog.objects.filter(user=request.user)
            #for specific query search 
            if request.GET.get('search'):
                search = request.GET.get('search')
                blog = blog.filter(Q(title__icontains = search)| Q(blog_text__icontains=search))
            serializer = blogSerializer(blog,many=True)
            return Response(
                {
                    'data':serializer.data,
                    'message':'Successfully get ALL the Blog'
                },status=status.HTTP_201_CREATED
            )
        except Exception as e:
            print(e)
            return Response(
                {
                    'data':serializer.errors,
                    'message':'Somethinng is went Wrong...'
                },status=status.HTTP_400_BAD_REQUEST
            )
    def patch(self,request):
        try:
            #get the data 
            data = request.data 
            blog = Blog.objects.filter(uid=data.get('uid'))
            #if not the blog exits 
            if not blog.exists:
                return Response(
                    {
                        'data':{},
                        'message':'Invalid Blogs uid'
                    },status=status.HTTP_400_BAD_REQUEST
                )
            #if its not the right user 
            if request.user != blog[0].user:
                return Response(
                    {
                        'data':{},
                        "message":'you are not allowed to update this blog'
                    },status=status.HTTP_400_BAD_REQUEST
                )
            serializer = blogSerializer(blog[0],data=data,partial=True)
            if not serializer.is_valid():
                return Response(
                    {
                        'data':serializer.errors,
                        'message':'Something went Wrong...'
                    },status=status.HTTP_400_BAD_REQUEST
                )
            serializer.save()
            return Response(
                {
                    'data':serializer.data,
                    'message':'Blog is updated Successfully..'
                },status=status.HTTP_200_OK
            )
            
        except Exception as e:
            print(e)
            return Response(
                {
                    'data':{},
                    'message':'Something is went Wrong...'
                },status=status.HTTP_400_BAD_REQUEST
            )
    def delete(self,request):
        try:
            data = request.data 
            blog = Blog.objects.filter(uid=data['uid'])
            if not blog.exists:
                return Response(
                    {
                        'data':{},
                        'message':'The Blog is Not exists'
                    },status=status.HTTP_400_BAD_REQUEST
                )
            if request.user != blog[0].user:
                return Response(
                    {
                        'data':{},
                        'message': 'You are not allowed to Delete This Blog'
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            blog[0].delete()
            return Response(
                {
                    'data':{},
                    "message":'Successfully Delete the Blog...'
                },status=status.HTTP_200_OK
            )
        except Exception as e:
            print(e)
            return Response(
                {
                    'data':{},
                    'message':'Something went wrong...'
                },status=status.HTTP_400_BAD_REQUEST
            )
    
#create Public View 
class PublicApi(APIView):
    def get(self,request):
        try:
            blog = Blog.objects.all().order_by('?')
            #for specific query search 
            if request.GET.get('search'):
                search = request.GET.get('search')
                blog = blog.filter(Q(title__icontains = search)| Q(blog_text__icontains=search))
            page_number = request.GET.get('page',1)
            paginator = Paginator(blog, 5)
            serializer = blogSerializer(paginator.page(page_number),many=True)
            return Response(
                {
                    'data':serializer.data,
                    'message':'Successfully get ALL the Blog'
                },status=status.HTTP_201_CREATED
            )
        except Exception as e:
            print(e)
            return Response(
                {
                    'data':{},
                    'message':'Invalid Page Number'
                },status=status.HTTP_400_BAD_REQUEST
            )
        