def total_carro(request):
    ttl=0
    ctd=0
    if "carrito_de_compra" in request.session:
        for key,value in request.session["carrito_de_compra"].items():
            ttl = ttl + float(value["precio_total"])
            ctd = ctd + int(value["pedido_total"])
    else:    
        carrito_de_compra=request.session["carrito_de_compra"]={}        
        
    return {"context_total":ttl,"context_cant":ctd}    