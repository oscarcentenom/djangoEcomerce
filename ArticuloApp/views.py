from django.shortcuts import render, HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from ArticuloApp.models import Producto
import requests
# Create your views here.

class HomeView(View):
    @method_decorator(csrf_exempt)
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    #   get y post
def home(request):
    prod=Producto.objects.all()
    
    return render(request,"ArticuloApp/home.html", {"productos": prod})

def Articulo(request,pro_id):
    
    prod=Producto.objects.get(id=pro_id)
    reciente_vista_producto = None
    # Vistas de articulos recientes
    
    if "reciente_vista" in request.session:
        if pro_id in request.session["reciente_vista"]:
            request.session["reciente_vista"].remove(pro_id) 
        reciente_vista_producto=Producto.objects.filter(pk__in=request.session["reciente_vista"])
        
        request.session["reciente_vista"].insert(0,pro_id)
        if len(request.session["reciente_vista"]) > 5:
            request.session["reciente_vista"].pop()
    else:
         request.session["reciente_vista"] = [pro_id] 
    request.session.modified = True
    #..................
    context={"productos": prod,"reciente_vista_producto":reciente_vista_producto} 
    
    return render(request,"ArticuloApp/Articulo.html/",context)