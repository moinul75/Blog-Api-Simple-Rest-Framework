from django.urls import path,include



urlpatterns = [
    path('account/',include('Account.urls')),
    path('home/',include('Home.urls')),
]
