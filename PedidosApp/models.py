from django.db import models
from django.contrib.auth import get_user_model
from ArticuloApp.models import Producto
from django.db.models import F, FloatField

User = get_user_model()

# Create your models here.
class Pedidos(models.Model):
    usr_ped= models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    nombre_ped = models.CharField(max_length=100, verbose_name="Nombres")
    apellido_ped = models.CharField(max_length=100, verbose_name="Apellidos")
    correo_ped = models.CharField(max_length=100, verbose_name="Email")
    tele_ped = models.CharField(max_length=100, verbose_name="Telefono")
    dir_ped = models.CharField(max_length=100, verbose_name="Direccion")
    ciudad_ped = models.CharField(max_length=100, verbose_name="Ciudad")
    estado_ped = models.CharField(max_length=100, verbose_name="Estado")
    zip_ped = models.CharField(max_length=100, verbose_name="Zip")
    creado_ped= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)

    @property
    def total(self):
        return self.DetallePedido_set.aggregate(
           total=sum(F("precio_Producto")*F("cant_Producto"), output_field=FloatField())
            
            
        )["total"]
    
    class Meta:
        verbose_name="Pedido"
        verbose_name_plural="Pedidos"
        db_table="Pedidos"
        ordering=["id"]
        
class DetallePedidos(models.Model):
    Ped= models.ForeignKey(Pedidos,null=True,blank=True,on_delete=models.CASCADE) 
    Product = models.ForeignKey(Producto,null=True,blank=True,on_delete=models.CASCADE)
    precio_Producto = models.IntegerField() 
    cant_Producto = models.IntegerField()
    
    def __str__(self):
        return f"{self.cant_Producto} und. de {self.Producto.nombre_prod}"
    
    class Meta:
        verbose_name="DetallePedidos"
        verbose_name_plural="Detalle Pedidos"
        db_table="Detalle Pedidos"
        ordering=["id"]