from django.urls import path 
from .views import BlogApi,PublicApi

urlpatterns = [
    path('blog',BlogApi.as_view()),
    path('',PublicApi.as_view()),
]
