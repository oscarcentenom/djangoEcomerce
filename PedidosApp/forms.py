from django import forms
from .models import Pedidos, DetallePedidos

class Dir_Form(forms.ModelForm):
    class Meta:
        model = Pedidos
        fields = ["nombre_ped","apellido_ped",
                  "correo_ped","tele_ped","dir_ped",
                  "ciudad_ped","estado_ped","zip_ped"]
