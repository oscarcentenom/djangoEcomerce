from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Pedidos,DetallePedidos
from .forms import Dir_Form
from django.contrib.auth import get_user_model
from ArticuloApp.models import Producto
# Create your views here. 

@login_required(login_url="/")

def Transaccion(request):
    
    # la session
    if "carrito_de_compra" in request.session:
        carrito_de_compra=request.session["carrito_de_compra"]
    else:    
        carrito_de_compra=request.session["carrito_de_compra"]={}
        
    # FORMULARIO   
    if request.method == "POST":   
        form_pedido=Dir_Form(data=request.POST)
        if form_pedido.is_valid():
            User = request.user
            pedido=Pedidos.objects.create(usr_ped=User,nombre_ped=request.POST["nombre_ped"],apellido_ped=request.POST["apellido_ped"],correo_ped=request.POST["correo_ped"],tele_ped=request.POST["tele_ped"],dir_ped=request.POST["dir_ped"],ciudad_ped=request.POST["ciudad_ped"],estado_ped=request.POST["estado_ped"],zip_ped=request.POST["zip_ped"])
            #form_ped.save()
            lista_pedidos=list()
            
            for key,value in carrito_de_compra.items():
                print("--------",pedido)
                lista_pedidos.append(DetallePedidos(
                Ped_id=str(pedido),
                Product_id=key,    
                precio_Producto=value["precio_prod"],
                cant_Producto=value["pedido_total"]    
                ))
                prod=Producto.objects.get(id=key)
                prod.cantidad_prod=int(prod.cantidad_prod)-int(value["pedido_total"])
                prod.save()
            DetallePedidos.objects.bulk_create(lista_pedidos)
            request.session["carrito_de_compra"]={}
            return redirect("Home")
    else:
        
        form_pedido = Dir_Form()    
        return render(request, "CarroApp/Transaccion.html/", {"carro":carrito_de_compra, "form":form_pedido})