from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from ArticuloApp.models import Producto
import requests
from django.contrib import messages



"""def Transaccion(request):
    if "carrito_de_compra" in request.session:
        carrito_de_compra=request.session["carrito_de_compra"]
    else:    
        carrito_de_compra=request.session["carrito_de_compra"]={}
    return render(request, "CarroApp/Transaccion.html/", {"carro":carrito_de_compra})"""

def Card(request):
    if "carrito_de_compra" in request.session:
        carrito_de_compra=request.session["carrito_de_compra"]
    else:    
        carrito_de_compra=request.session["carrito_de_compra"]={}
    return render(request, "ArticuloApp/Carro.html/", {"carro":carrito_de_compra})
def Carro(request,pro_id):
    prod=Producto.objects.get(id=pro_id)
    carrito_de_compra=request.session.get("carrito_de_compra", default=None)
    if "carrito_de_compra" in request.session:
        carrito_de_compra=request.session["carrito_de_compra"]
        
        if str(pro_id) in request.session["carrito_de_compra"]:
            carrito_de_compra=request.session["carrito_de_compra"]
        else:
            pedido=[]
            for i in range(prod.cantidad_prod): 
                if i <= prod.cantidad_prod:
                   if i <= 11:
                      pedido.append(i+1)  
                 
            carrito_de_compra[pro_id]={
                "id":str(prod.id),
                #"categoria_prod":prod.categoria_prod,
                "ref_prod":prod.ref_prod,
                "nombre_prod":prod.nombre_prod,
                "imagen_prod":prod.imagen_prod.url,
                "descripcion_prod":prod.descripcion_prod,
                #"tipo_prod":prod.tipo_prod,
                "oferta_prod":str(prod.oferta_prod),
                "precio_prod":str(prod.precio_prod),
                "cantidad_prod":str(prod.cantidad_prod),
                "pedido":pedido,
                "pedido_total":1,
                "precio_total":str(prod.precio_prod)
            }
    else:
        carrito_de_compra=request.session["carrito_de_compra"]={}
        
    #del carrito_de_compra[21]   
    #carrito_de_compra=request.session["carrito_de_compra"]={} 
    request.session.modified = True
    #carro.clear()
    print("..............",carrito_de_compra)
    
    return render(request, "ArticuloApp/Carro.html/", {"carro":carrito_de_compra})

def Act(request,pro_id):
    prod=Producto.objects.get(id=pro_id)
    carrito_de_compra=request.session["carrito_de_compra"]
    carrito_de_compra[str(pro_id)]["pedido_total"]=str(request.POST["valor"])
    carrito_de_compra[str(pro_id)]["precio_total"]=int(carrito_de_compra[str(pro_id)]["precio_prod"])*int(carrito_de_compra[str(pro_id)]["pedido_total"])
    #del carrito_de_compra[str(pro_id)]
    request.session.modified = True
    #print(".......gg.......",carrito_de_compra[str(pro_id)])
    messages.success(request,"Actualizado")
    return render(request, "ArticuloApp/Carro.html/", {"carro":carrito_de_compra})

def Eliminar(request,pro_id):
    prod=Producto.objects.get(id=pro_id)
    carrito_de_compra=request.session["carrito_de_compra"]
    if str(pro_id) in request.session["carrito_de_compra"]:
        del carrito_de_compra[str(pro_id)]
    request.session.modified = True
    print(".......gg.......",carrito_de_compra)
    return render(request, "ArticuloApp/Carro.html/", {"carro":carrito_de_compra})