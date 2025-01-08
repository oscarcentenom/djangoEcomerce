"""from django.contrib.auth.models import Group, User
from ArticuloApp.models import Producto
from rest_framework import permissions, viewsets
from .serializers import GroupSerializer, UserSerializer, ProductoSerializer
"""

"""      Con clases
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    """
    
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.models import User  
from rest_framework.authtoken.models import Token
from rest_framework import status  
from django.shortcuts import get_object_or_404
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


# Con funciones

@api_view(["POST"])
def login (request):
    user=get_object_or_404(User, username=request.data["username"])
    if not user.check_password(request.data["password"]):
        print(request.data["password"])
        return Response({"error":"Invalido password"}, status=status.HTTP_400_BAD_REQUEST)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({"token":token.key, "user":serializer.data},status=status.HTTP_200_OK)

@api_view(["POST"])
def register(request):
    #print(request.data)
    serializer=UserSerializer(data=request.data)
    if serializer.is_valid():
       serializer.save()
       user=User.objects.get(username=serializer.data["username"])
       user.set_password(serializer.data["password"])
       user.save()   # Usuario createdo
       #creamos el Token
       token=Token.objects.create(user=user)
       return Response({"token":token.key,"user":serializer.data},status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile (request):
    
    print(request.user.id)
    serializer = UserSerializer(instance=request.user)
    
    #return Response("Tu estas logeado como {}".format(request.user.username), status=status.HTTP_200_OK)
    return Response(serializer.data, status=status.HTTP_200_OK)
