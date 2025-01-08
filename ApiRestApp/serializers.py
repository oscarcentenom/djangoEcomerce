from django.contrib.auth.models import Group, User
from ArticuloApp.models import Producto
from rest_framework import serializers


class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"
        #fields = ['nombre_prod', 'precio_prod', 'cantidad_prod', 'descripcion_prod']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']