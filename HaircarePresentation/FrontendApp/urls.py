from django.urls import path
from FrontendApp import views

urlpatterns = [
    path('home/',views.home, name="home")
]