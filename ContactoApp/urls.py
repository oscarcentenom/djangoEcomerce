from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('Register_cont/', views.Register_cont, name="Register_cont"),
    ]
