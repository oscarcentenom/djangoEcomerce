from django.contrib.auth.models import Group, User
from ArticuloApp.models import Producto
from rest_framework import permissions, viewsets
from .serializers import GroupSerializer, UserSerializer, ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows productos to be viewed or edited.
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]