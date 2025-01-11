from django.db import models

# Create your models here.
class Tipo_NU(models.Model):
    tipo=models.CharField(max_length=20, verbose_name="Tipo")
    activo_tipo=models.BooleanField()
    
    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name="Tipo"
        verbose_name_plural="Tipos"
        db_table="Tipo"
        #ordering=["nombre_categ","-activo_categ"]


class Categoria(models.Model):
    nombre_categ=models.CharField(max_length=20, verbose_name="Categoria")
    activo_categ=models.BooleanField()
    
    def __str__(self):
        return self.nombre_categ

    class Meta:
        verbose_name="Categoria"
        verbose_name_plural="Categorias"
        db_table="Categoria"
        #ordering=["nombre_categ","-activo_categ"]


class Producto(models.Model):
    categoria_prod = models.ForeignKey(Categoria,null=True,blank=True,on_delete=models.CASCADE)
    ref_prod=models.CharField(max_length=15,verbose_name="Ref.")
    nombre_prod=models.CharField(max_length=100, verbose_name="Nombre del Articulo")
    imagen_prod=models.ImageField(upload_to="ArticuloApp")
    descripcion_prod=models.CharField(max_length=200)
    tipo_prod=models.ForeignKey(Tipo_NU,null=True,blank=True,on_delete=models.CASCADE)
    oferta_prod=models.IntegerField(blank=True, null=True)
    precio_prod=models.DecimalField(default=0, decimal_places=2, max_digits=10)
    cantidad_prod=models.IntegerField()
    creado_prod= models.DateTimeField(auto_now_add=True)
    actualizado_prod=models.DateTimeField(auto_now_add=True)
    activo_prod=models.BooleanField()
    
    def __str__(self):
        return self.nombre_prod
    
    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"
        db_table="Productos"

   
class ImagenesSegundarias(models.Model):
    imagen_segundarias=models.ImageField(upload_to="ArticuloApp")
    product=models.ForeignKey(Producto,null=True,blank=True,on_delete=models.CASCADE, related_name="imagenes")
    
    def __str__(self):
        return str(self.imagen_segundarias)
    
    class Meta:
        verbose_name="ImagenesSegundaria"
        verbose_name_plural="ImagenesSegundarias"
        db_table="ImagenesSegundaria"
        #ordering=["nombre_categ","-activo_categ"]        
