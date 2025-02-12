"""from django.urls import include, path
from rest_framework import routers
from . import views"""

#router = routers.DefaultRouter()
#router.register(r'productos', views.ProductoViewSet)
#router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)
#router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
"""
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]"""

from django.urls import path
from . import views

urlpatterns = [
    path('Login', views.login, name="Login"),
    path('Registro', views.registro, name="Registro"),
    path('Profile', views.profile, name="Profile"),
    ]