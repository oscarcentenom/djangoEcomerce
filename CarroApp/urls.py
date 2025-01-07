from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('Carro/<int:pro_id>/', views.Carro, name="Carro"),
    path('Carro/Eliminar/<int:pro_id>/', views.Eliminar, name="Eliminar"),
    path('Carro/Act/<int:pro_id>/', views.Act, name="Act"),
    path('Card/', views.Card, name="Card"),
    #path('Transaccion/', views.Transaccion, name="Transaccion"),
]
