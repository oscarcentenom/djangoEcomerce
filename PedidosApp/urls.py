from django.contrib import admin
from django.urls import path
from .views import Transaccion
from . import views

urlpatterns = [
    #path('Procesar_pedido/', views.Procesar_pedido, name="Procesar_pedido"),
    path('Transaccion/', views.Transaccion, name="Transaccion"),
]
