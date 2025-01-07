from django import forms
from .models import Contactos


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contactos
        fields = ["nombre_contacto","correo_contacto",
                  "asunt_contacto","msj_contacto"]

