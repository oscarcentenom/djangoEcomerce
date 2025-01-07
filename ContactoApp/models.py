from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Contactos(models.Model):
    usr_contacto= models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    nombre_contacto = models.CharField(max_length=100, verbose_name="Nombre y apellido:")
    correo_contacto = models.CharField(max_length=100, verbose_name="Email:")
    asunt_contacto = models.CharField(max_length=100, verbose_name="Asunto:")
    msj_contacto = models.TextField(max_length=255, verbose_name="Mensaje:")
    
    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name="Contacto"
        verbose_name_plural="Contactos"
        db_table="Contactos"
        ordering=["id"]