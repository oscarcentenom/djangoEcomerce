from django.contrib import admin
from django.urls import path
from .views import VRegister,Logear,cerrar_login,VRegister_aut,Logear_aut
from . import views


urlpatterns = [
    path('Register/',VRegister.as_view(), name="Register"), 
    path('Logear/',Logear, name="Logear"),
    path('Cerrar_login/',cerrar_login, name="Cerrar_login"),
    path('Register_aut/',VRegister_aut.as_view(), name="Register_aut"),
    path('Logear_aut/',Logear_aut, name="Logear_aut"),
]