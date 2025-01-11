from django.shortcuts import render, HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from ArticuloApp.models import Producto, ImagenesSegundarias
import requests
from django.core.paginator import Paginator

# Create your views here.

class HomeView(View):
    @method_decorator(csrf_exempt)
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    #   get y post
def home(request):
    prod=Producto.objects.all()
    paginator = Paginator(prod, 4)
    
    numero_pagina = request.GET.get("page") or 1
    page_obj = paginator.get_page(numero_pagina)
    actual_pagina=int(numero_pagina)
    paginas=range(1,page_obj.paginator.num_pages + 1)
    return render(request,"ArticuloApp/home.html", {"productos": page_obj, 
                                                    "page_obj": page_obj,
                                                    "paginas": paginas,
                                                    "actual_pagina": actual_pagina
                                                    })

def Articulo(request,pro_id):
    
    prod=Producto.objects.get(id=pro_id)
    imag=ImagenesSegundarias.objects.filter(product=pro_id)
    for key in imag:
        print("xxxxxxxx    ",key)
    
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
    context={"productos": prod,"reciente_vista_producto":reciente_vista_producto,"imag":imag} 
    print(context)
    return render(request,"ArticuloApp/Articulo.html/",context)