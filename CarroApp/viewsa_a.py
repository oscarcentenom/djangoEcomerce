from django.shortcuts import render, HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from ArticuloApp.models import Producto
import requests

def CarroSession(request,pro_id):
    prod=Producto.objects.get(id=pro_id)
    carrito_de_compra=request.session.get("carrito_de_compra", default=None)
    
    if "carrito_de_compra" in request.session:
        carrito_de_compra=request.session["carrito_de_compra"]
        print("tamaño ",len(carrito_de_compra))
        print(request.session["carrito_de_compra"])
        
        for key,value in request.session["carrito_de_compra"].items():
            print("..............",value["id"])   
            if pro_id == value["id"]:
                pass
            carrito_de_compra=request.session["carrito_de_compra"]
    else:
        carro=request.session["carrito_de_compra"]={}
        print("..............",carrito_de_compra)
    #del carrito_de_compra["clav"]    
    request.session.modified = True
    #carro.clear()
    
    
    return render(request, "ArticuloApp/Carro.html/", {"carro":carrito_de_compra})
    
    
    """
    prod=Producto.objects.get(id=pro_id)
    reciente_vista_producto = None
    # Vistas de articulos recientes
    
    if "carro" in request.session:
        if pro_id in request.session["carro"]:
            #request.session["carro"].remove(pro_id)
            print("....carro in.....") 
        query_del_carro=Producto.objects.filter(pk__in=request.session["carro"])
        print("objeto queryset del carro", query_del_carro)
        request.session["carro"].insert(0,pro_id)

        #if len(request.session["carro"]) > 5:
        #    request.session["carro"].pop()
        #    print("....pop.....")
    else:
         request.session["carro"] = [pro_id] 
         print("....pro_id.....", [pro_id])
         
    request.session.modified = True
    #..................
    for key in query_del_carro:
        print(key.descripcion_prod)
    return render(request,"ArticuloApp/Carro.html/")

"""



    """
    def add_to_cart(request, item):
    # Retrieve the user's cart from the session, or create a new one
        cart = request.session.get('cart', [])

    # Add the selected item to the cart
        cart.append(item)

    # Update the session data
        request.session['cart'] = cart

    # Render the updated cart
    return render(request, 'cart/cart.html', {'cart': cart})
    """